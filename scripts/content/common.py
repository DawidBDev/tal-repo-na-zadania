def theory(before, title, text, example):
    return dict(before=before, title=title, text=text, example=example)


def task(title, prompt, solution, tests, hint):
    return dict(title=title, prompt=prompt, solution=solution, tests=tests, hint=hint)


def lesson(number, slug, title, destination, recall, theories, tasks, official=None):
    assert len(tasks) == 10
    return dict(number=number, slug=slug, title=title, destination=destination,
                recall=recall, theories=theories, tasks=tasks, official=official)
