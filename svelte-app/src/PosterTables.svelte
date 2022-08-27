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
    sessions={[{label:"1PA-", items:range(1,16)}]}
    on:search />
<PosterTable title={"Room 2216"}
    sessions={[{label:"1PA-", items:range(17,32)}]}
    on:search />
<PosterTable title={"Room 2201"}
    sessions={[{label:"1PA-", items:range(33,48)}]}
    on:search />
<PosterTable title={"Room 2202"}
    sessions={[{label:"1PA-", items:range(49,64)}]}
    on:search />
<PosterTable title={"Room 2203"}
    sessions={[{label:"1PA-", items:range(65,80)}]}
    on:search />
<PosterTable title={"Room 2204"}
    sessions={[
        {label:"1PA-", items:range(81,89)},
        {label:"1PB-", items:range(1,7)},
    ]}
    on:search />
<PosterTable title={"Room 2207"}
    sessions={[
        {label:"1PB-", items:range(8,16)},
        {label:"1PC-", items:range(1,7)},
    ]}
    on:search />
<PosterTable title={"Room 2208"}
    sessions={[
        {label:"1PC-", items:range(8,13)},
        {label:"1PD-", items:range(1,10)},
    ]}
    on:search />
<PosterTable title={"Room 2209"}
    sessions={[
        {label:"1PD-", items:range(11,17)},
        {label:"1PE-", items:range(1,9)},
    ]}
    on:search />
<PosterTable title={"Room 2210"}
    sessions={[
        {label:"1PE-", items:range(10,11)},
        {label:"1PF-", items:range(1,14)},
    ]}
    on:search />
<PosterTable title={"Room 2211"}
    sessions={[
        {label:"1PF-", items:range(15,30)},
    ]}
    on:search />
<PosterTable title={"Room 2212"}
    sessions={[
        {label:"1PF-", items:range(31,47)},
    ]}
    on:search />
