<script lang="ts">
    import { _ } from 'svelte-i18n';
    import SmartTable from './smarttable.svelte';

    let table
    _.subscribe(t=>{

        const centerzone2 = "<a href='https://www.kyushu-u.ac.jp/ja/campus/ito/'>"+t("centerzone2")+"</a>"
        const mainhall    = "<a href='https://www.marinemesse.or.jp/congress/access/'>"+t("mainhall")+"</a>"
        const hotelokura  = "<a href='https://www.fuk.hotelokura.co.jp/access/'>"+t("hotelokura")+"</a>"

        table=[
            [t("Date"), t("Time"), t("Event"), t("Access")],
            [t("sept26"), "9:20-11:50", t("Morning sessions"), centerzone2],
            [t("sept26"), "12:50-14:50", t("Poster sessions"), centerzone2],
            [t("sept26"), "15:00-19:00", t("Afternoon sessions"), centerzone2],

            [t("sept27"), "9:20-11:50", t("Morning sessions"), centerzone2],
            [t("sept27"), "12:50-14:50", t("Poster sessions"), centerzone2],
            [t("sept27"), "15:00-15:30", t("Award lectures"), centerzone2],
            [t("sept27"), "15:40-18:50", t("Afternoon sessions"), centerzone2],

            [t("sept28"), "8:50-15:30", t("Award lectures"), mainhall],
            [t("sept28"), "15:40-16:50", t("JSCC general meeting"), mainhall],
            [t("sept28"), "17:30-19:30", t("Banquet"), hotelokura],
        ];
    })

</script>

<div class="post">
    <SmartTable {table} />
</div>

<style>
    div.post {
        margin: 2px;
    }
</style>
