<script lang="ts">
    import { _ } from 'svelte-i18n';
</script>

<div class="textbox">
    <h2>{$_("Abstract book")}</h2>
    <ul>
        <li>
            {$_("msg1")}
        </li>
        <li>
            (link here)
        </li>
    </ul>
    <h2>{$_("Seat reservation for the banquet")}</h2>
    <ul>
        <li>
            {$_("msg2")}
        </li>
        <li>
            <a href="http://www.chem.okayama-u.ac.jp/~reg/seat72/">http://www.chem.okayama-u.ac.jp/~reg/seat72/</a>
        </li>
    </ul>
</div>


<style>
    .textbox {
        padding: 10px;

        /* for children */
        display: block;
        flex-flow: row;
        flex-wrap: wrap;
        justify-content: left;
    }
</style>
