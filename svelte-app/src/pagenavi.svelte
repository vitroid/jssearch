<script>
    import { createEventDispatcher } from 'svelte';
	const dispatch = createEventDispatcher();

    export let page = 0;
    export let highlight = false;
    let color = "white";

    $: {
        color = ( highlight ? "#eee" : "#fff" );
    }

	function buttonPressed() {
        // invoke signal
		dispatch('pagenavi', {
			text: page
		});
	}

</script>

<button on:click={buttonPressed} style="--color:{color}" >
    {page+1}
</button>

<style>
    button {
        background-color: var(--color);
    }
</style>