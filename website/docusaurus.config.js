// @ts-check
import { themes as prismThemes } from 'prism-react-renderer';


/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'Physical AI & Humanoid Robotics',
  tagline: 'An Embodied Intelligence Textbook',
  favicon: 'img/favicon.ico',

  future: {
    v4: true,
  },

  // GitHub Pages config
  url: 'https://muhammad-aashib.github.io', // your GitHub Pages URL
  baseUrl: '/MY_BOOK/', // repo name as baseUrl
  organizationName: 'MUHAMMAD-AASHIB', // GitHub username
  projectName: 'MY_BOOK', // repo name

  onBrokenLinks: 'throw',

  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      ({
        docs: {
          sidebarPath: './sidebars.js',
          editUrl:
            'https://github.com/MUHAMMAD-AASHIB/MY_BOOK/tree/main/',
        },
        blog: {
          showReadingTime: true,
          editUrl:
            'https://github.com/MUHAMMAD-AASHIB/MY_BOOK/tree/main/',
        },
        theme: {
          customCss: './src/css/custom.css',
        },
      }),
    ],
  ],

  themeConfig: ({
    image: 'img/docusaurus-social-card.jpg',
    colorMode: {
      respectPrefersColorScheme: true,
    },
    navbar: {
      title: 'Physical AI & Humanoid Robotics',
      logo: {
        alt: 'Book Logo',
        src: 'img/logo.svg',
      },
      items: [
        { type: 'docSidebar', sidebarId: 'tutorialSidebar', position: 'left', label: 'Book' },
        { to: '/blog', label: 'Blog', position: 'left' },
        { href: 'https://github.com/MUHAMMAD-AASHIB/MY_BOOK', label: 'GitHub', position: 'right' },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Docs',
          items: [{ label: 'Tutorial', to: '/docs/intro' }],
        },
        {
          title: 'Community',
          items: [
            { label: 'Stack Overflow', href: 'https://stackoverflow.com/questions/tagged/docusaurus' },
            { label: 'Discord', href: 'https://discordapp.com/invite/docusaurus' },
            { label: 'X', href: 'https://x.com/docusaurus' },
          ],
        },
        {
          title: 'More',
          items: [
            { label: 'Blog', to: '/blog' },
            { label: 'GitHub', href: 'https://github.com/MUHAMMAD-AASHIB/MY_BOOK' },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} MUHAMMAD-AASHIB. Built with Docusaurus.`,
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
    },
  }),
};

export default config;
