import rss from "@astrojs/rss";
import { getCollection } from "astro:content";
import { siteMeta } from "../data/profile";

export async function GET(context: { site: URL | undefined }) {
  const posts = (await getCollection("blog", ({ data }) => !data.draft)).sort(
    (a, b) => b.data.publishedAt.valueOf() - a.data.publishedAt.valueOf()
  );

  const site = context.site ?? siteMeta.siteUrl;

  return rss({
    title: `${siteMeta.title} Blog`,
    description: "Technical writing on backend systems, enterprise software, and practical AI delivery.",
    site,
    items: posts.map((post) => ({
      title: post.data.title,
      description: post.data.description,
      pubDate: post.data.publishedAt,
      link: `/blog/${post.id}/`,
      categories: post.data.tags
    })),
    customData: `<language>en-us</language>`
  });
}
