import { localStorageStore } from "@babichjacob/svelte-localstorage/browser";
export const marks = localStorageStore("marks", new Set());

import { data } from './index.js';

export const all_talks = new Set(data.map(record=>{return record.lab}))
console.log(all_talks)
