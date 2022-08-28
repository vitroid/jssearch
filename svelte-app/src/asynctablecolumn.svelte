<script lang="ts">
    import VButton from "./vbutton.svelte";
    export let column
    export let label

    $: {

    }
</script>

<div class="container">
    <div class="head">
        {label}
    </div>
    {#each column as button, i}
    <VButton id={button.id} label={button.label} height={button.bin[2]} on:search />
    {/each}
</div>

<style>
    .container {
        display: flex;
        flex-direction: column;
        justify-content: start;
    }
    .head {
        font-weight: bold;
        text-align: center;
    }
</style>
