<script lang="ts">
    import { _ } from 'svelte-i18n';
    let schedule
    _.subscribe(t=>{
        schedule=[
        [t("sept26"), "9:20-11:50", t("Morning sessions"), t("centerzone2")],
        [t("sept26"), "12:50-14:50", t("Poster sessions"), t("centerzone2")],
        [t("sept26"), "15:00-19:00", t("Afternoon sessions"), t("centerzone2")],

        [t("sept27"), "9:20-11:50", t("Morning sessions"), t("centerzone2")],
        [t("sept27"), "12:50-14:50", t("Poster sessions"), t("centerzone2")],
        [t("sept27"), "15:00-15:30", t("Award lectures"), t("centerzone2")],
        [t("sept27"), "15:40-18:50", t("Afternoon sessions"), t("centerzone2")],

        [t("sept28"), "8:50-15:30", t("Award lectures"), t("mainhall")],
        [t("sept28"), "15:40-16:50", t("JSCC general meeting"), t("mainhall")],
        [t("sept28"), "17:30-19:30", t("Banquet"), t("hotelokura")],
    ]})
</script>

<div class="post">
    <h1 class="post-title">{$_("General Information")}</h1>
    <p class="intro">{$_("Overall schedule")}</p>
    <table>
        <tbody>
            {#each schedule as row}
            <tr>
                {#each row as col, i}
                <td class={"col"+i}>
                    {col}
                </td>
                {/each}
            </tr>
            {/each}
        </tbody>
    </table>
</div>

<style>
    div.post {
        margin: 2px;
        /* justify-content: center; */
    }
    h1.post-title {
        /* padding: 10px; */
        text-align: center;
        font-size: 120%;
        /* background-color: #fff; */
    }
    p.intro {
        padding: 5px;
        text-align: center;
        font-size: 120%;
        font-weight: bold;
    }
    table {
        margin-left: auto;
        margin-right: auto;
        background-color: #ddd;
    }
    tr {
        /* border: 1px solid #888; */
        background-color: #fff;
        margin: 0;
    }
    .col1 {
        text-align: center;
    }
</style>
