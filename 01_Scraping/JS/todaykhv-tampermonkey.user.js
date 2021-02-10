// ==UserScript==
// @name         todaykhv
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  Data extraction example
// @author       akumidv
// @match        https://todaykhv.ru/
// @grant        none
// ==/UserScript==

(function() {
    'use strict';

    const newsHeads = document.querySelectorAll('.itemNewsWrap .itemNewsHead > a')
    const firstHeadText = newsHeads[1].innerText;

    console.log('Всего заголовков:', newsHeads.length)
    console.log('Заголовок первого элемента:', firstHeadText)

    // Сохраняем данные в файл
    const saveLink = document.createElement('a');
    saveLink.href = 'data:text,Всего заголовков ' + newsHeads.length + '\nЗаголовок первого элемента ' + firstHeadText;
    saveLink.download = "data.txt";
    saveLink.click();
})();