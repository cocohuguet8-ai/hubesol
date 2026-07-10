import { defineCollection, z } from 'astro:content';

const lessons = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    description: z.string(),
    level: z.string(),
    hub: z.string(),
    hubSlug: z.string(),
    answerBox: z.string(),
    answerLead: z.string().optional(),
    answerPoints: z.array(z.string()).optional(),
    answerNote: z.string().optional(),
    quiz: z.string().optional(),
    faq: z.array(z.object({ q: z.string(), a: z.string() })).default([]),
    teacherObjectives: z.array(z.string()).default([]),
    related: z.array(z.object({ title: z.string(), href: z.string() })).default([]),
    draft: z.boolean().default(false),
  }),
});

export const collections = { lessons };
