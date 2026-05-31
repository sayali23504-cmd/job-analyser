def build_interview_markdown(path: str, sections: dict[str, list[str]]) -> None:
    lines: list[str] = ["# Interview Preparation Sheet", ""]
    for section, questions in sections.items():
        lines.append(f"## {section}")
        if not questions:
            lines.append("- No questions generated yet")
        else:
            for q in questions:
                lines.append(f"- {q}")
        lines.append("")

    with open(path, "w", encoding="utf-8") as file:
        file.write("\n".join(lines))
