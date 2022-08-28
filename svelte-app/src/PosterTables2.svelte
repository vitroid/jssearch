<script lang="ts">
    import PosterTable from "./postertable.svelte";

    function range(a,b){
        let c = new Set();
        for(let i=a; i<=b; i++){
            c.add(i);
        }
        return c;
    }
</script>

<PosterTable title={"Room 2215"}
    sessions={[{label:"2PA-", items:range(1,16)}]}
    on:search />
<PosterTable title={"Room 2216"}
    sessions={[{label:"2PA-", items:range(17,32)}]}
    on:search />
<PosterTable title={"Room 2201"}
    sessions={[{label:"2PA-", items:range(33,48)}]}
    on:search />
<PosterTable title={"Room 2202"}
    sessions={[{label:"2PA-", items:range(49,64)}]}
    on:search />
<PosterTable title={"Room 2203"}
    sessions={[{label:"2PA-", items:range(65,80)}]}
    on:search />
<PosterTable title={"Room 2204"}
    sessions={[
        {label:"2PA-", items:range(81,88)},
        {label:"2PB-", items:range(1,8)},
    ]}
    on:search />
<PosterTable title={"Room 2207"}
    sessions={[
        {label:"2PB-", items:range(9,16)},
        {label:"2PC-", items:range(1,8)},
    ]}
    on:search />
<PosterTable title={"Room 2208"}
    sessions={[
        {label:"2PC-", items:range(9,12)},
        {label:"2PD-", items:range(1,12)},
    ]}
    on:search />
<PosterTable title={"Room 2209"}
    sessions={[
        {label:"2PD-", items:range(13,18)},
        {label:"2PE-", items:range(1,10)},
    ]}
    on:search />
<PosterTable title={"Room 2210"}
    sessions={[
        {label:"2PE-", items:range(11,12)},
        {label:"2PF-", items:range(1,14)},
    ]}
    on:search />
<PosterTable title={"Room 2211"}
    sessions={[
        {label:"2PF-", items:range(15,30)},
    ]}
    on:search />
<PosterTable title={"Room 2212"}
    sessions={[
        {label:"2PF-", items:range(31,46)},
    ]}
    on:search />
