from scipub.domain.text import normalize_title


def main() -> None:
    print("scipub 0.1.0 — середовище налаштовано")
    print(normalize_title("  Deep   Learning  IN  Science "))


if __name__ == "__main__":
    main()
