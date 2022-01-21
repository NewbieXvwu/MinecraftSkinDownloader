module.exports = {
  // 站点配置
  lang: 'zh-CN',
  title: 'MinecraftSkinDownloader',
  description: '这是一个可以简单地下载任何Minecraft正版玩家的皮肤的软件，使用Python编写，由NewbieXvwu维护。',

  // 主题和它的配置
  theme: '@vuepress/theme-default',
  themeConfig: {
    logo: '/docs/logo.png',
  },
  head: [['link', { rel: 'icon', href: '/docs/logo.png' }]],
  base: "/MinecraftSkinDownloader/"
}