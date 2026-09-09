// Zgodność ze wcześniejszym poleceniem; nie utrzymujemy drugiej kopii treści.
import { spawnSync } from "node:child_process";
import { fileURLToPath } from "node:url";

const generator = fileURLToPath(new URL("./build-course.py", import.meta.url));
const python = process.env.PYTHON || (process.platform === "win32" ? "python" : "python3");
const result = spawnSync(python, [generator], { stdio: "inherit" });
if (result.error) {
    console.error("Nie udało się uruchomić Pythona:", result.error.message);
    process.exit(1);
}
process.exit(result.status ?? 1);
