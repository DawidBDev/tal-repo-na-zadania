(() => {
    "use strict";

    const course = window.PYTHON_COURSE;

    if (!course || !Array.isArray(course.lessons)) {
        document.body.innerHTML = "<main class=\"noscript-message\">Nie udało się wczytać treści prezentacji.</main>";
        return;
    }

    const elements = {
        stage: document.querySelector("#stage"),
        slide: document.querySelector("#slide"),
        headerLocation: document.querySelector("#header-location"),
        previousLesson: document.querySelector("#previous-lesson"),
        nextLesson: document.querySelector("#next-lesson"),
        previousSection: document.querySelector("#previous-section"),
        nextSection: document.querySelector("#next-section"),
        progressValue: document.querySelector("#progress-value"),
        slideCounter: document.querySelector("#slide-counter"),
        verticalRail: document.querySelector("#vertical-rail"),
        menuButton: document.querySelector("#menu-button"),
        closeMenuButton: document.querySelector("#close-menu-button"),
        drawer: document.querySelector("#lesson-drawer"),
        drawerBackdrop: document.querySelector("#drawer-backdrop"),
        lessonList: document.querySelector("#lesson-list"),
        lessonSearch: document.querySelector("#lesson-search"),
        helpButton: document.querySelector("#help-button"),
        helpDialog: document.querySelector("#help-dialog"),
        closeHelpButton: document.querySelector("#close-help-button"),
        fullscreenButton: document.querySelector("#fullscreen-button"),
        printButton: document.querySelector("#print-button"),
        toast: document.querySelector("#toast")
    };

    const state = {
        horizontal: 0,
        vertical: 0,
        direction: "enter-right",
        drawerOpen: false,
        toastTimer: null,
        touchStartX: 0,
        touchStartY: 0,
        touchActive: false
    };

    const pythonKeywords = new Set([
        "False", "None", "True", "and", "as", "assert", "async", "await", "break",
        "class", "continue", "def", "del", "elif", "else", "except", "finally", "for",
        "from", "global", "if", "import", "in", "is", "lambda", "nonlocal", "not",
        "or", "pass", "raise", "return", "try", "while", "with", "yield",
        "int", "str", "float", "bool", "list", "tuple", "dict", "set", "range",
        "len", "print", "sum", "min", "max", "sorted", "enumerate", "zip"
    ]);

    function escapeHtml(value) {
        return String(value)
            .replaceAll("&", "&amp;")
            .replaceAll("<", "&lt;")
            .replaceAll(">", "&gt;")
            .replaceAll('"', "&quot;")
            .replaceAll("'", "&#039;");
    }

    function plainText(value) {
        return value
            .replace(/`([^`]+)`/g, "$1")
            .replace(/\*\*([^*]+)\*\*/g, "$1")
            .replace(/\[([^\]]+)\]\([^)]+\)/g, "$1")
            .trim();
    }

    function inlineMarkdown(value) {
        const codeTokens = [];
        let text = String(value).replace(/`([^`]+)`/g, (_, code) => {
            const token = `@@INLINE_CODE_${codeTokens.length}@@`;
            codeTokens.push(`<code>${escapeHtml(code)}</code>`);
            return token;
        });

        text = escapeHtml(text);
        text = text.replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>");
        text = text.replace(/\[([^\]]+)\]\((https?:\/\/[^\s)]+|mailto:[^\s)]+|(?:\.\/)?(?:materialy-zrodlowe|karty)\/[^\s)]+)\)/g, (_, label, href) => {
            return `<a href="${href}" target="_blank" rel="noopener noreferrer">${label}</a>`;
        });

        codeTokens.forEach((token, index) => {
            text = text.replace(`@@INLINE_CODE_${index}@@`, token);
        });

        return text;
    }

    function highlightPython(source) {
        const tokenPattern = /("""[\s\S]*?"""|'''[\s\S]*?'''|"(?:\\.|[^"\\])*"|'(?:\\.|[^'\\])*'|#[^\n]*|\b\d+(?:\.\d+)?(?:[eE][+-]?\d+)?\b|\b[A-Za-z_]\w*\b)/gm;
        let result = "";
        let previousEnd = 0;

        for (const match of source.matchAll(tokenPattern)) {
            result += escapeHtml(source.slice(previousEnd, match.index));
            const token = match[0];
            let className = "";

            if (token.startsWith("#")) {
                className = "token-comment";
            }
            else if (token.startsWith('"') || token.startsWith("'")) {
                className = "token-string";
            }
            else if (/^\d/.test(token)) {
                className = "token-number";
            }
            else if (pythonKeywords.has(token)) {
                className = "token-keyword";
            }

            result += className
                ? `<span class="${className}">${escapeHtml(token)}</span>`
                : escapeHtml(token);
            previousEnd = match.index + token.length;
        }

        result += escapeHtml(source.slice(previousEnd));
        return result;
    }

    function splitTableRow(line) {
        const cells = [];
        let current = "";
        let insideCode = false;
        const trimmed = line.trim().replace(/^\|/, "").replace(/\|$/, "");

        for (const character of trimmed) {
            if (character === "`") {
                insideCode = !insideCode;
                current += character;
            }
            else if (character === "|" && !insideCode) {
                cells.push(current.trim());
                current = "";
            }
            else {
                current += character;
            }
        }

        cells.push(current.trim());
        return cells;
    }

    function isTableDelimiter(line) {
        const cells = splitTableRow(line);
        return cells.length > 0 && cells.every(cell => /^:?-{3,}:?$/.test(cell));
    }

    function startsBlock(lines, index) {
        const line = lines[index] ?? "";

        return line.trim() === ""
            || /^```/.test(line.trim())
            || /^#{1,4}\s+/.test(line)
            || /^>\s?/.test(line)
            || /^\s*[-*]\s+/.test(line)
            || /^\s*\d+\.\s+/.test(line)
            || (/^\s*\|/.test(line) && isTableDelimiter(lines[index + 1] ?? ""))
            || /^-{3,}\s*$/.test(line);
    }

    function markdownToHtml(markdown) {
        const lines = String(markdown).replace(/\r\n/g, "\n").split("\n");
        const html = [];
        let index = 0;
        let codeNumber = 0;

        while (index < lines.length) {
            const line = lines[index];

            if (line.trim() === "") {
                index++;
                continue;
            }

            const fenceMatch = line.trim().match(/^```([\w+-]*)/);

            if (fenceMatch) {
                const language = fenceMatch[1].toLowerCase();
                const code = [];
                index++;

                while (index < lines.length && !/^```\s*$/.test(lines[index].trim())) {
                    code.push(lines[index]);
                    index++;
                }

                if (index < lines.length) {
                    index++;
                }

                const rawCode = code.join("\n");
                const label = language === "python" ? "Python 3" : language === "text" ? "Dane / wynik" : language || "Kod";
                const highlighted = language === "python" ? highlightPython(rawCode) : escapeHtml(rawCode);

                html.push(
                    `<div class="code-frame" data-code-block="${codeNumber}">`
                    + `<div class="code-toolbar"><span>${escapeHtml(label)}</span>`
                    + `<button class="copy-code" type="button" data-copy-code="${codeNumber}">Kopiuj</button></div>`
                    + `<pre><code class="language-${escapeHtml(language || "text")}">${highlighted}</code></pre>`
                    + `</div>`
                );
                codeNumber++;
                continue;
            }

            const headingMatch = line.match(/^(#{1,4})\s+(.+)$/);

            if (headingMatch) {
                const level = Math.max(2, Math.min(4, headingMatch[1].length));
                html.push(`<h${level}>${inlineMarkdown(headingMatch[2])}</h${level}>`);
                index++;
                continue;
            }

            if (/^\s*\|/.test(line) && isTableDelimiter(lines[index + 1] ?? "")) {
                const headers = splitTableRow(line);
                index += 2;
                const rows = [];

                while (index < lines.length && /^\s*\|/.test(lines[index])) {
                    rows.push(splitTableRow(lines[index]));
                    index++;
                }

                html.push(
                    "<div class=\"table-wrap\"><table><thead><tr>"
                    + headers.map(cell => `<th>${inlineMarkdown(cell)}</th>`).join("")
                    + "</tr></thead><tbody>"
                    + rows.map(row => `<tr>${row.map(cell => `<td>${inlineMarkdown(cell)}</td>`).join("")}</tr>`).join("")
                    + "</tbody></table></div>"
                );
                continue;
            }

            const unorderedMatch = line.match(/^\s*[-*]\s+(.+)$/);
            const orderedMatch = line.match(/^\s*\d+\.\s+(.+)$/);

            if (unorderedMatch || orderedMatch) {
                const ordered = Boolean(orderedMatch);
                const items = [];
                const pattern = ordered ? /^\s*\d+\.\s+(.+)$/ : /^\s*[-*]\s+(.+)$/;
                const firstNumber = ordered ? Number(line.match(/^\s*(\d+)\./)?.[1]) : 1;

                while (index < lines.length) {
                    const itemMatch = lines[index].match(pattern);

                    if (!itemMatch) {
                        break;
                    }

                    items.push(itemMatch[1]);
                    index++;
                }

                const tag = ordered ? "ol" : "ul";
                const startAttribute = ordered && firstNumber !== 1 ? ` start="${firstNumber}"` : "";
                html.push(`<${tag}${startAttribute}>${items.map(item => `<li>${inlineMarkdown(item)}</li>`).join("")}</${tag}>`);
                continue;
            }

            if (/^>\s?/.test(line)) {
                const quote = [];

                while (index < lines.length && /^>\s?/.test(lines[index])) {
                    quote.push(lines[index].replace(/^>\s?/, ""));
                    index++;
                }

                html.push(`<blockquote>${inlineMarkdown(quote.join(" "))}</blockquote>`);
                continue;
            }

            if (/^-{3,}\s*$/.test(line)) {
                html.push("<hr>");
                index++;
                continue;
            }

            const paragraph = [line.trim()];
            index++;

            while (index < lines.length && !startsBlock(lines, index)) {
                paragraph.push(lines[index].trim());
                index++;
            }

            html.push(`<p>${inlineMarkdown(paragraph.join(" "))}</p>`);
        }

        return html.join("\n");
    }

    function lessonAt(horizontal) {
        return horizontal > 0 ? course.lessons[horizontal - 1] : null;
    }

    function maximumVertical(horizontal) {
        const lesson = lessonAt(horizontal);
        return lesson ? lesson.sections.length : 0;
    }

    function courseTitleMarkup() {
        const title = escapeHtml(course.meta.title).replace("Python", "<span>Python</span>");

        return `
            <div class="slide-inner">
                <span class="course-kicker">Kurs • ${escapeHtml(course.meta.standard)}</span>
                <h1 class="course-title">${title}</h1>
                <div class="course-meta">
                    <span>Prowadzący: <strong>${escapeHtml(course.meta.teacher)}</strong></span>
                    <a href="mailto:${escapeHtml(course.meta.email)}">${escapeHtml(course.meta.email)}</a>
                </div>
                <div class="keyboard-map" aria-label="Skrócona instrukcja sterowania">
                    <span><kbd>←</kbd> <kbd>→</kbd> zmiana lekcji</span>
                    <span><kbd>↑</kbd> <kbd>↓</kbd> elementy lekcji</span>
                    <span><kbd>M</kbd> spis lekcji</span>
                    <span><kbd>F</kbd> pełny ekran</span>
                </div>
                <div class="download-links">
                    <a class="secondary-button" href="kurs-python.zip" download>Pobierz cały kurs · ZIP</a>
                    <span>12 kart · 96 zadań na lekcji + 24 po lekcji</span>
                </div>
            </div>`;
    }

    function lessonOverviewMarkup(lesson) {
        const topics = lesson.sections.map((section, index) => ({ ...section, vertical: index + 1 }))
            .filter(section => ["recall", "theory", "matura"].includes(section.kind))
            .map(section => `<li><a href="${routeFor(lesson.number, section.vertical)}">${inlineMarkdown(section.title)}</a></li>`).join("");

        return `
            <div class="slide-inner">
                <span class="lesson-number">Lekcja ${lesson.number} · 60 minut</span>
                <h1 class="lesson-title">${escapeHtml(lesson.title)}</h1>
                <p class="lesson-summary">Użyj strzałki w dół, aby przechodzić przez kolejne elementy tej lekcji.</p>
                <div class="download-links">
                    <a class="secondary-button" href="${escapeHtml(lesson.download)}" download>Pobierz kartę Jupyter</a>
                    <a href="kurs-python.zip" download>Cały kurs z danymi</a>
                </div>
                <ol class="topic-cloud">${topics}</ol>
            </div>`;
    }

    function contentSlideMarkup(lesson, section) {
        const typeLabel = section.kind === "exercise"
            ? "Zadania na lekcji"
            : section.kind === "homework"
                ? "Praca samodzielna"
                : section.kind === "solution"
                    ? "Rozwiązanie wzorcowe"
                : section.kind === "matura"
                    ? "Oryginalne zadanie maturalne"
                : `Lekcja ${lesson.number}`;
        const context = section.context
            ? `<p class="slide-context">Do tematu: ${inlineMarkdown(section.context)}</p>`
            : "";

        const body = section.markdown.replace(/^## [^\n]+\n+/, "");
        const content = `<div class="markdown-body">${markdownToHtml(body)}</div>`;
        const displayed = section.kind === "solution"
            ? `<details class="solution-reveal"><summary>Pokaż rozwiązanie i testy</summary>${content}</details>`
            : content;
        return `
            <div class="slide-inner">
                <header class="slide-heading">
                    <span class="slide-type">${typeLabel}</span>
                    <h1>${inlineMarkdown(section.title)}</h1>
                    ${context}
                </header>
                ${displayed}
            </div>`;
    }

    function buildSlide(horizontal, vertical) {
        if (horizontal === 0) {
            return {
                className: "slide title-slide",
                html: courseTitleMarkup()
            };
        }

        const lesson = lessonAt(horizontal);

        if (vertical === 0) {
            return {
                className: lesson.kind === "organization"
                    ? "slide lesson-overview organization-overview"
                    : "slide lesson-overview",
                html: lessonOverviewMarkup(lesson)
            };
        }

        const section = lesson.sections[vertical - 1];
        const kindClass = section.kind === "exercise"
            ? " task-slide"
            : section.kind === "homework"
                ? " homework-slide"
                : section.kind === "organization"
                    ? " organization-slide"
                : "";

        return {
            className: `slide content-slide${kindClass}`,
            html: contentSlideMarkup(lesson, section)
        };
    }

    function routeFor(horizontal, vertical) {
        const lesson = lessonAt(horizontal);
        return lesson ? `#/${lesson.number}/${vertical}` : "#/start";
    }

    function readRoute() {
        const route = window.location.hash.replace(/^#\/?/, "");

        if (!route || route === "start") {
            return { horizontal: 0, vertical: 0 };
        }

        const [lessonPart, sectionPart = "0"] = route.split("/");
        const lessonNumber = Number(lessonPart);
        const horizontal = course.lessons.findIndex(lesson => lesson.number === lessonNumber) + 1;

        if (horizontal <= 0) {
            return { horizontal: 0, vertical: 0 };
        }

        const requestedSection = Number(sectionPart);
        const vertical = Number.isFinite(requestedSection)
            ? Math.max(0, Math.min(Math.trunc(requestedSection), maximumVertical(horizontal)))
            : 0;
        return { horizontal, vertical };
    }

    function updateRoute() {
        const route = routeFor(state.horizontal, state.vertical);

        if (window.location.hash !== route) {
            history.replaceState(null, "", route);
        }
    }

    function flattenedProgress() {
        const total = 1 + course.lessons.reduce((sum, lesson) => sum + lesson.sections.length + 1, 0);

        if (state.horizontal === 0) {
            return { current: 0, total };
        }

        const previous = course.lessons
            .slice(0, state.horizontal - 1)
            .reduce((sum, lesson) => sum + lesson.sections.length + 1, 0);
        return { current: 1 + previous + state.vertical, total };
    }

    function updateLessonList() {
        elements.lessonList.querySelectorAll(".lesson-link").forEach(button => {
            button.classList.toggle("active", Number(button.dataset.horizontal) === state.horizontal);
        });
    }

    function renderVerticalRail() {
        elements.verticalRail.replaceChildren();
        const lesson = lessonAt(state.horizontal);

        if (!lesson) {
            return;
        }

        const labels = lesson.kind === "exam"
            ? [lesson.title]
            : ["Początek lekcji", ...lesson.sections.map(section => plainText(section.title))];

        labels.forEach((label, vertical) => {
            const button = document.createElement("button");
            const section = vertical > 0 ? lesson.sections[vertical - 1] : null;
            button.type = "button";
            button.className = "rail-dot";
            button.title = label;
            button.setAttribute("aria-label", `${vertical + 1}. ${label}`);

            if (vertical === state.vertical) {
                button.classList.add("active");
                button.setAttribute("aria-current", "step");
            }

            if (section?.kind === "exercise") {
                button.classList.add("task-dot");
            }
            else if (section?.kind === "homework") {
                button.classList.add("homework-dot");
            }
            else if (section?.kind === "organization") {
                button.classList.add("organization-dot");
            }

            button.addEventListener("click", () => navigate(state.horizontal, vertical, vertical > state.vertical ? "enter-down" : "enter-up"));
            elements.verticalRail.append(button);
        });

        elements.verticalRail.querySelector(".active")?.scrollIntoView({ block: "nearest" });
    }

    function updateInterface() {
        const lesson = lessonAt(state.horizontal);
        const maximum = maximumVertical(state.horizontal);
        const progress = flattenedProgress();

        elements.previousLesson.disabled = state.horizontal === 0;
        elements.nextLesson.disabled = state.horizontal === course.lessons.length;
        elements.previousSection.disabled = !lesson || state.vertical === 0;
        elements.nextSection.disabled = !lesson || state.vertical === maximum;
        elements.progressValue.style.width = `${progress.total <= 1 ? 0 : progress.current / (progress.total - 1) * 100}%`;

        if (!lesson) {
            elements.headerLocation.textContent = "Strona tytułowa";
            elements.slideCounter.textContent = "Start";
            document.title = course.meta.title;
        }
        else {
            const locationLabel = lesson.kind === "exam" ? "Spotkanie" : "Lekcja";
            elements.headerLocation.textContent = `${locationLabel} ${lesson.number} · ${lesson.title}`;
            elements.slideCounter.textContent = lesson.kind === "exam"
                ? `Sprawdzian · 1/1`
                : `Lekcja ${lesson.number} · ${state.vertical + 1}/${maximum + 1}`;
            document.title = `${locationLabel} ${lesson.number}: ${lesson.title}`;
        }

        updateLessonList();
        renderVerticalRail();
    }

    function attachCopyButtons() {
        elements.slide.querySelectorAll("[data-copy-code]").forEach(button => {
            button.addEventListener("click", async () => {
                const frame = button.closest(".code-frame");
                const code = frame?.querySelector("code")?.textContent ?? "";

                try {
                    await navigator.clipboard.writeText(code);
                    showToast("Kod skopiowany");
                }
                catch {
                    const area = document.createElement("textarea");
                    area.value = code;
                    area.style.position = "fixed";
                    area.style.opacity = "0";
                    document.body.append(area);
                    area.select();
                    document.execCommand("copy");
                    area.remove();
                    showToast("Kod skopiowany");
                }
            });
        });
    }

    function render() {
        const built = buildSlide(state.horizontal, state.vertical);
        elements.slide.className = `${built.className} ${state.direction}`.trim();
        elements.slide.innerHTML = built.html;
        elements.slide.scrollTop = 0;
        attachCopyButtons();
        updateInterface();
        updateRoute();
    }

    function navigate(horizontal, vertical, direction) {
        const safeHorizontal = Math.max(0, Math.min(horizontal, course.lessons.length));
        const safeVertical = Math.max(0, Math.min(vertical, maximumVertical(safeHorizontal)));

        if (safeHorizontal === state.horizontal && safeVertical === state.vertical) {
            return;
        }

        state.horizontal = safeHorizontal;
        state.vertical = safeVertical;
        state.direction = direction;
        render();
    }

    function changeLesson(delta) {
        const target = state.horizontal + delta;
        navigate(target, 0, delta > 0 ? "enter-right" : "enter-left");
    }

    function changeSection(delta) {
        navigate(
            state.horizontal,
            state.vertical + delta,
            delta > 0 ? "enter-down" : "enter-up"
        );
    }

    function showToast(message) {
        clearTimeout(state.toastTimer);
        elements.toast.textContent = message;
        elements.toast.classList.add("visible");
        state.toastTimer = setTimeout(() => elements.toast.classList.remove("visible"), 1600);
    }

    function buildLessonList() {
        const fragment = document.createDocumentFragment();

        course.lessons.forEach((lesson, index) => {
            const button = document.createElement("button");
            button.type = "button";
            button.className = lesson.kind === "exam"
                ? "lesson-link exam-link"
                : lesson.kind === "organization"
                    ? "lesson-link organization-link"
                    : "lesson-link";
            button.dataset.horizontal = String(index + 1);
            button.dataset.search = `${lesson.number} ${lesson.title}`.toLocaleLowerCase("pl");
            button.innerHTML = `<span class="lesson-link-number">${String(lesson.number).padStart(2, "0")}</span>`
                + `<span class="lesson-link-title">${escapeHtml(lesson.title)}</span>`;
            button.addEventListener("click", () => {
                const direction = index + 1 >= state.horizontal ? "enter-right" : "enter-left";
                navigate(index + 1, 0, direction);
                closeDrawer();
            });
            fragment.append(button);
        });

        elements.lessonList.append(fragment);
    }

    function openDrawer() {
        if (state.drawerOpen) {
            return;
        }

        state.drawerOpen = true;
        elements.drawerBackdrop.hidden = false;
        elements.drawer.setAttribute("aria-hidden", "false");
        elements.drawer.inert = false;
        elements.menuButton.setAttribute("aria-expanded", "true");
        requestAnimationFrame(() => elements.drawer.classList.add("open"));
        setTimeout(() => elements.lessonSearch.focus(), 220);
    }

    function closeDrawer() {
        if (!state.drawerOpen) {
            return;
        }

        state.drawerOpen = false;
        elements.drawer.classList.remove("open");
        elements.drawer.setAttribute("aria-hidden", "true");
        elements.drawer.inert = true;
        elements.menuButton.focus();
        elements.menuButton.setAttribute("aria-expanded", "false");
        setTimeout(() => {
            if (!state.drawerOpen) {
                elements.drawerBackdrop.hidden = true;
            }
        }, 220);
    }

    async function toggleFullscreen() {
        try {
            if (!document.fullscreenElement) {
                await document.documentElement.requestFullscreen();
            }
            else {
                await document.exitFullscreen();
            }
        }
        catch {
            showToast("Tryb pełnoekranowy jest niedostępny");
        }
    }

    function renderPrintDeck() {
        document.querySelector(".print-deck")?.remove();
        const printDeck = document.createElement("main");
        printDeck.className = "print-deck";

        const cover = buildSlide(0, 0);
        printDeck.insertAdjacentHTML("beforeend", `<article class="print-slide title-slide">${cover.html}</article>`);

        course.lessons.forEach((lesson, lessonIndex) => {
            for (let vertical = 0; vertical <= lesson.sections.length; vertical++) {
                const built = buildSlide(lessonIndex + 1, vertical);
                printDeck.insertAdjacentHTML("beforeend", `<article class="print-slide ${built.className.replace("slide", "")}">${built.html}</article>`);
            }
        });

        document.body.append(printDeck);
        printDeck.querySelectorAll("details").forEach(details => { details.open = true; });
        closeDrawer();
        requestAnimationFrame(() => window.print());
    }

    function handleKeyboard(event) {
        const target = event.target;

        if (event.key === "Escape" && state.drawerOpen) {
            event.preventDefault();
            closeDrawer();
            return;
        }

        if (target instanceof HTMLInputElement || target instanceof HTMLTextAreaElement || target?.isContentEditable) {
            return;
        }

        if (state.drawerOpen && event.key !== "Escape") {
            return;
        }

        if (elements.helpDialog.open && event.key !== "Escape") {
            return;
        }

        switch (event.key) {
            case "ArrowLeft":
                event.preventDefault();
                changeLesson(-1);
                break;
            case "ArrowRight":
                event.preventDefault();
                changeLesson(1);
                break;
            case "ArrowUp":
                event.preventDefault();
                changeSection(-1);
                break;
            case "ArrowDown":
                event.preventDefault();
                changeSection(1);
                break;
            case "Home":
                event.preventDefault();
                navigate(0, 0, "enter-left");
                break;
            case "Escape":
                closeDrawer();
                break;
            case "f":
            case "F":
                event.preventDefault();
                toggleFullscreen();
                break;
            case "m":
            case "M":
                event.preventDefault();
                openDrawer();
                break;
            case "?":
                event.preventDefault();
                elements.helpDialog.showModal();
                break;
        }
    }

    elements.previousLesson.addEventListener("click", () => changeLesson(-1));
    elements.nextLesson.addEventListener("click", () => changeLesson(1));
    elements.previousSection.addEventListener("click", () => changeSection(-1));
    elements.nextSection.addEventListener("click", () => changeSection(1));
    elements.menuButton.addEventListener("click", openDrawer);
    elements.closeMenuButton.addEventListener("click", closeDrawer);
    elements.drawerBackdrop.addEventListener("click", closeDrawer);
    elements.helpButton.addEventListener("click", () => elements.helpDialog.showModal());
    elements.closeHelpButton.addEventListener("click", () => elements.helpDialog.close());
    elements.fullscreenButton.addEventListener("click", toggleFullscreen);
    elements.printButton.addEventListener("click", renderPrintDeck);

    elements.lessonSearch.addEventListener("input", () => {
        const query = elements.lessonSearch.value.trim().toLocaleLowerCase("pl");

        elements.lessonList.querySelectorAll(".lesson-link").forEach(button => {
            button.hidden = query !== "" && !button.dataset.search.includes(query);
        });
    });

    elements.helpDialog.addEventListener("click", event => {
        if (event.target === elements.helpDialog) {
            elements.helpDialog.close();
        }
    });

    elements.stage.addEventListener("pointerdown", event => {
        state.touchActive = false;
        if (event.pointerType !== "touch" || event.target.closest("pre, a, button, summary")) {
            return;
        }

        state.touchStartX = event.clientX;
        state.touchStartY = event.clientY;
        state.touchActive = true;
    });

    elements.stage.addEventListener("pointerup", event => {
        if (event.pointerType !== "touch" || !state.touchActive) {
            return;
        }
        state.touchActive = false;

        const differenceX = event.clientX - state.touchStartX;
        const differenceY = event.clientY - state.touchStartY;

        if (Math.max(Math.abs(differenceX), Math.abs(differenceY)) < 55) {
            return;
        }

        if (Math.abs(differenceX) > Math.abs(differenceY)) {
            changeLesson(differenceX < 0 ? 1 : -1);
        }
        else if (elements.slide.scrollHeight <= elements.slide.clientHeight + 1) {
            changeSection(differenceY < 0 ? 1 : -1);
        }
    });

    window.addEventListener("keydown", handleKeyboard);
    window.addEventListener("hashchange", () => {
        const route = readRoute();
        state.horizontal = route.horizontal;
        state.vertical = route.vertical;
        state.direction = "";
        render();
    });
    window.addEventListener("afterprint", () => document.querySelector(".print-deck")?.remove());

    buildLessonList();
    Object.assign(state, readRoute());
    render();
})();
