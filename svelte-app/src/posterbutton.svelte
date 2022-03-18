<script>
    import { marks } from "./mark.js";
    import { directory } from "./directory.js";
    import { createEventDispatcher } from 'svelte';
	const dispatch = createEventDispatcher();

    export let label;
    export let row;
    export let order;
    export let items;

    let active = true;
    let color = "#888";
    let id;
    $: {
        id=label + row + order;
        let item = row*10+order;
        active = items.has(item);
    }

	function buttonPressed() {
        // invoke signal
		dispatch('search', {
			text: id
		});
	}

    export function mark() {
        console.log(id, "marked")
    }

</script>

<button bind:this={directory[id]} disabled={!active} on:click={buttonPressed} style="--color: {color}">
    <!-- {id} -->
</button>

<style>
    button {
        width: 20px;
        height: 20px;
    }
    button:disabled{
        border: 0;
    }
</style>
