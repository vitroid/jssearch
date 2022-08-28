import App from './App.svelte';



import { addMessages, locale } from 'svelte-i18n';

import { cn } from './cn.js';
import { en } from './en.js';
import { ja } from './ja.js';
addMessages('ja', ja);
addMessages('en', en);
addMessages('cn', cn);

// register('en', () => import('./en.js'));
// register('ja', () => import('./ja.js'));

// init({
//     fallbackLocale: 'en',
//     initialLocale: getLocaleFromNavigator(),
// });

// locale.set(getLocaleFromNavigator())
locale.set("ja")

var app = new App({
	target: document.body
});

export default app;
