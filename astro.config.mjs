import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';
import rehypeProTip from './scripts/rehype-pro-tip.mjs';

export default defineConfig({
  site: 'https://hubesol.com',
  trailingSlash: 'always',
  integrations: [sitemap()],
  markdown: { rehypePlugins: [rehypeProTip] },
});
