#  Skill Review Tool
### 8-Dimension Hermes / Claude Code Skill Auditor

<p align="center">
  <img src="https://img.shields.io/badge/python-3.6+-blue" alt="Python 3.6+" />
  <img src="https://img.shields.io/badge/license-MIT-green" alt="MIT License" />
  <img src="https://img.shields.io/badge/status-stable-brightgreen" alt="Stable" />
  <img src="https://img.shields.io/badge/dependencies-zero-orange" alt="Zero Dependencies" />
</p>

<p align="center">
  A professional skill auditing tool that scores Hermes Agent / Claude Code skills across <strong>8 dimensions</strong>.
  <br/>
  Supports GitHub URL or local directory, outputs terminal summary + rich HTML report.
</p>

---

##   What it does

```bash
# Audit any skill on GitHub
python review_tool.py https://github.com/lamwon/hermes-image-generation-skill --html

# Open the report
open skill-review-report.html
```

You get:

```
  代码质量     [####------] 4.0/10
  文档完整性    [#########-] 9.0/10
  ...

  >>> 总分: 7.0/10  评级: B <<<

  改进建议:
    1. 增加 try/except 错误处理
    2. 添加 --help 参数说明
    ...
```

Plus a full **HTML report** with:

-   Repo info (stars, topics, description)
-   File structure overview
-   8-dimension bar chart with color-coded scores
-   Total score + letter grade (S/A/B/C/D)
-   Sorted improvement suggestions

---

##   Quick Start

### 1. Clone or download

```bash
git clone https://github.com/lamwon/hermes-skill-review.git
cd hermes-skill-review
```

### 2. Audit a skill

```bash
# Terminal summary only
python review_tool.py https://github.com/lamwon/hermes-image-generation-skill

# With HTML report
python review_tool.py https://github.com/lamwon/hermes-image-generation-skill --html

# Custom output path
python review_tool.py https://github.com/user/repo --html -o my-report.html

# Local directory
python review_tool.py /path/to/skill/folder --html
```

### 3. Install as Hermes Skill

```bash
hermes skills install lamwon/hermes-skill-review
```

Then in Hermes:

```
/review-skill https://github.com/lamwon/hermes-image-generation-skill
```

Or in conversation:

```
帮我审查这个技能：https://github.com/xxx/skill-name
```

---

##   8-Dimension Framework

| # | Dimension | Weight | What it checks |
|---|-----------|--------|----------------|
| 1 | **Code Quality** | 1.0x | Syntax correctness, error handling, security, style |
| 2 | **Documentation** | 1.0x | README/SKILL.md completeness, install guide, examples, FAQ |
| 3 | **Architecture** | 0.8x | File structure, dependency management, engineering config |
| 4 | **User Experience** | 0.9x | Ease of install, intuitive args, Chinese-friendly output |
| 5 | **Error Handling** | 0.8x | Retry logic, rate limit handling, edge cases |
| 6 | **Portability** | 0.6x | Cross-platform (Windows/Mac/Linux), encoding, paths |
| 7 | **Maintainability** | 0.6x | Comments, centralized config, versioning |
| 8 | **Innovation** | 0.5x | Unique value, differentiation, comparison tables |

**Grading:** S (9-10) > A (8-9) > B (7-8) > C (5-7) > D (<5)

---

##   HTML Report Preview

The HTML report features a dark theme with:

- Color-coded rating badge (S/A/B/C/D)
- Repo metadata card
- File structure tags
- Animated score bars
- Actionable improvement suggestions
- Print-friendly layout

---

##   Requirements

- Python 3.6+ (standard library only — no pip install needed)
- Internet access (for GitHub URL mode only)

---

##   Use Cases

| Who | When to use |
|-----|-------------|
| **Skill authors** | Before publishing to get objective feedback |
| **Skill reviewers** | To quickly evaluate PRs / submissions |
| **Team leads** | To enforce quality standards across skills |
| **Learners** | To understand what makes a good skill |

---

##   License

MIT
