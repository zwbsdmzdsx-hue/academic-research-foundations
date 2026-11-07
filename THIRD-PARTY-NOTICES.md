# React Bits 动效来源与许可

本教材的 `v2/motion.js` 是为本网站编写的轻量原生适配，参考 React Bits 的三项组件机制。没有加载 React、GSAP、外部脚本或字体，也没有将上游组件作为单独组件包分发。

核对日期：2026-11-08。上游：[DavidHDev/react-bits](https://github.com/DavidHDev/react-bits)，修订 `4dc7b5b7772e1217c8fb8d2a7aa074302180e5b4`（2026-10-31）。

| 上游组件 | 教材中的用途 | 本地适配 |
| --- | --- | --- |
| [AnimatedContent](https://github.com/DavidHDev/react-bits/blob/4dc7b5b7772e1217c8fb8d2a7aa074302180e5b4/src/content/Animations/AnimatedContent/AnimatedContent.jsx) | 首页文字和原创几何图首次入场 | Web Animations API；10px轻移、初始不透明度0.65；正文不入场动画；不循环 |
| [FadeContent](https://github.com/DavidHDev/react-bits/blob/4dc7b5b7772e1217c8fb8d2a7aa074302180e5b4/src/content/Animations/FadeContent/FadeContent.jsx) | 用户主动展开答案、术语和章节 | 仅220ms透明度变化；无模糊、噪声或滚动触发 |
| [ClickSpark](https://github.com/DavidHDev/react-bits/blob/4dc7b5b7772e1217c8fb8d2a7aa074302180e5b4/src/content/Animations/ClickSpark/ClickSpark.jsx) | 开始阅读、已读、自测和复制操作的短反馈 | 保留三次缓出和径向短线机制；6根墨色短线、400ms、至多3组；不跟随指针 |

所有效果尊重系统“减弱动态效果”，切到后台或打印时停止；缺少相关浏览器能力时直接保留静态内容。上游代码快照仅保留在本地 `.firecrawl/` 中用于核查。

以下为上游完整许可。该许可包含 Commons Clause 条件，不能简称为纯 MIT。

---

MIT + Commons Clause License Condition v1.0

Copyright (c) 2026 David Haz

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, and distribute the Software **as part of an application, website, or product**, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

## Commons Clause Restriction

You may use this Software, including for any commercial purpose, **so long as you do not sell, sublicense, or redistribute the components themselves-whether alone, in a bundle, or as a ported version.**

The same restriction covers the React Bits tools (Background Studio, Texture Lab, Shape Magic, Center Stage, Sound Lab and any tools added later) and the sounds in the sound library. **You may not sell, sublicense, or redistribute the tools or the sounds themselves, or offer the tools or a substantially similar copy of them as a hosted service-whether alone, in a bundle, or as a ported version.**

What you make with the tools is yours to use. You can use exported code, images, videos, and audio files in any personal or commercial application, website, or product, including paid ones. **You may not sell or redistribute the exports on their own, either individually or as the product itself, such as a sound, texture, background, or template pack.**

## No Warranty

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
