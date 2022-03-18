<script>
    import { createEventDispatcher } from 'svelte';
	const dispatch = createEventDispatcher();

    export let label;
    export let query;

    function search() {
        // invoke signal
		dispatch('search', {
			text: query
		});

    }
</script>

<button on:click={search} >
    {label}
</button>

<style>
    /*大きな文字のリンクボタン*/
    button {
        border-radius: 5px 5px 5px;
        border: 1px solid #ccc;
        font-size: 120%;
        font-weight: bold;
        padding: 4px;
        color: black;
        background-color: white;
        text-decoration: none;
        margin-right: 3px;
        /* line-height: 150%; */
    }

</style>