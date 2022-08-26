<script>
    import { shortcuts } from "./jscc72";
    import ShortCut from "./shortcut.svelte";
</script>

<div>
{#each shortcuts as shortcut}
<ShortCut label={shortcut[0]} query={shortcut[1]} on:search />
{/each}
</div>
