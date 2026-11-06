# debug_modal_position.py
import subprocess
import os

script = """
const puppeteer = require('puppeteer');
(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.setViewport({ width: 390, height: 844 });
  await page.goto('file:///' + process.cwd().replace(/\\\\/g, '/') + '/index.html');
  await page.waitForTimeout(500);
  const rect = await page.evaluate(() => {
    const el = document.querySelector('#festive-modal > div');
    const b = el.getBoundingClientRect();
    return { x: b.x, y: b.y, width: b.width, height: b.height, windowWidth: window.innerWidth };
  });
  console.log('Rect:', JSON.stringify(rect));
  await browser.close();
})();
"""
with open('debug_pos.js', 'w', encoding='utf-8') as f:
    f.write(script)
