# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, "D:\\Hermes\\hermes-skill-review")

from review_tool import DIMENSIONS, generate_html

repo_data = {
    "full_name": "lamwon/hermes-image-generation-skill",
    "description": "DeepSeek V4 Flash prompt engineering + Flux free image generation",
    "stars": 0,
    "forks": 0,
    "language": "Python",
    "topics": ["deepseek", "flux", "image-generation", "hermes-agent", "ai-art", "siliconflow"],
    "contents": [".gitignore", "README.md", "SKILL.md", "image_workflow.py", "examples/", "SHARE_POSTS.md"],
}

scores = {
    "code_quality": {"name": "Code Quality", "name_cn": "\u4ee3\u7801\u8d28\u91cf", "score": 7.0, "weight": 1.0, "weighted": 7.0},
    "documentation": {"name": "Documentation", "name_cn": "\u6587\u6863\u5b8c\u6574\u6027", "score": 9.0, "weight": 1.0, "weighted": 9.0},
    "architecture": {"name": "Architecture", "name_cn": "\u67b6\u6784\u8bbe\u8ba1", "score": 7.5, "weight": 0.8, "weighted": 6.0},
    "ux": {"name": "User Experience", "name_cn": "\u7528\u6237\u4f53\u9a8c", "score": 7.5, "weight": 0.9, "weighted": 6.75},
    "error_handling": {"name": "Error Handling", "name_cn": "\u9519\u8bef\u5904\u7406", "score": 8.0, "weight": 0.8, "weighted": 6.4},
    "portability": {"name": "Portability", "name_cn": "\u8de8\u5e73\u53f0\u517c\u5bb9", "score": 7.0, "weight": 0.6, "weighted": 4.2},
    "maintainability": {"name": "Maintainability", "name_cn": "\u53ef\u7ef4\u62a4\u6027", "score": 6.5, "weight": 0.6, "weighted": 3.9},
    "innovation": {"name": "Innovation & Value", "name_cn": "\u521b\u65b0\u4ef7\u503c", "score": 7.0, "weight": 0.5, "weighted": 3.5},
}

result = {
    "scores": scores,
    "total_score": 7.4,
    "rating": "B",
    "suggestions": [
        "\u53ef\u4ee5\u8003\u8651\u6dfb\u52a0 --style \u53c2\u6570\u5207\u6362\u4e0d\u540c\u7684\u63d0\u793a\u8bcd\u98ce\u683c",
        "\u6dfb\u52a0\u56fe\u7247\u5bf9\u6bd4\u529f\u80fd\uff0c\u540c\u65f6\u751f\u6210\u591a\u5c3a\u5bf8\u5bf9\u6bd4\u56fe",
        "\u8003\u8651\u652f\u6301\u66f4\u591a\u7684 Flux \u6a21\u578b\u53d8\u4f53",
    ],
    "findings": [],
    "repo_data": repo_data,
    "timestamp": "2025-06-02 16:00",
}

html = generate_html(result)
with open("D:\\Hermes\\hermes-skill-review\\examples\\example-report.html", "w", encoding="utf-8") as f:
    f.write(html)
print("HTML report generated: examples/example-report.html")
print(f"Size: {len(html)} bytes")
