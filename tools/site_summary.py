class SiteEntry:
    def __init__(self, name, url, tags, description):
        self.name = name
        self.url = url
        self.tags = tags
        self.description = description

    def to_dict(self):
        return {
            "name": self.name,
            "url": self.url,
            "tags": self.tags,
            "description": self.description
        }


def load_sites():
    sites = [
        SiteEntry(
            name="HomeHTH",
            url="https://homehth.com.cn",
            tags=["华体会", "体育", "娱乐"],
            description="华体会体育娱乐平台，提供丰富的赛事与游戏体验。"
        ),
        SiteEntry(
            name="示例站点A",
            url="https://example-a.com",
            tags=["科技", "博客"],
            description="一个示例科技博客，分享前沿技术资讯。"
        ),
        SiteEntry(
            name="示例站点B",
            url="https://example-b.org",
            tags["教育", "开源"],
            description="开源教育平台，提供免费学习资源。"
        ),
        SiteEntry(
            name="示例站点C",
            url="https://example-c.net",
            tags=["生活", "社区"],
            description="生活社区论坛，交流日常经验。"
        ),
    ]
    return sites


def generate_summary(sites, keyword):
    matched = [site for site in sites if keyword in site.tags or keyword in site.name]
    if not matched:
        return f"未找到包含关键词「{keyword}」的站点。"
    
    lines = []
    lines.append(f"站点摘要（关键词：{keyword}）")
    lines.append("=" * 40)
    for idx, site in enumerate(matched, 1):
        lines.append(f"{idx}. 名称：{site.name}")
        lines.append(f"   URL：{site.url}")
        tags_str = ", ".join(site.tags)
        lines.append(f"   标签：{tags_str}")
        lines.append(f"   说明：{site.description}")
        lines.append("")
    return "\n".join(lines)


def main():
    sites = load_sites()
    keyword = "华体会"
    summary = generate_summary(sites, keyword)
    print(summary)


if __name__ == "__main__":
    main()