import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://hubesol.com',
  trailingSlash: 'always',
  integrations: [sitemap()],
});
