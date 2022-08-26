<script>
    import { Tab,TabList,TabPanel,Tabs } from './Components/Tabs/tabs.js';
    import { project } from './jscc72.js';
    import PosterTable from "./postertable.svelte";
    import SessionTable from "./sessiontable.svelte";

    function range(a,b){
        let c = new Set();
        for(let i=a; i<=b; i++){
            c.add(i);
        }
        return c;
    }

    // const poster1 = [ { label:"PA1-", items:range(1,74) },
    //                   { label:"PB1-", items:range(1,15) },
    //                   { label:"PC1-", items:range(1,16) },
    //                   { label:"PD1-", items:range(1,14) },
    //                   { label:"PE1-", items:range(1,10) },
    //                   { label:"PF1-", items:range(1,42) } ];

</script>

<Tabs>
    <TabList>
        <Tab>Sep. 26</Tab>
        <Tab>Sep. 27</Tab>
        <Tab>Sep. 28</Tab>
        <Tab>協賛企業</Tab>
    </TabList>

    <TabPanel>
        <div class="container">
            <div class="panel">
                <SessionTable title={"Oral session"}
                    sessions={project.sessions1}
                    timebins={project.bins_am}
                    slots={project.slots_am}
                    on:search />
            </div>
            <div class="panel">
                <PosterTable title={"2215"}
                    sessions={[{label:"1PA-", items:range(1,16)}]}
                    on:search />
                <PosterTable title={"2216"}
                    sessions={[{label:"1PA-", items:range(17,32)}]}
                    on:search />
                <PosterTable title={"2201"}
                    sessions={[{label:"1PA-", items:range(33,48)}]}
                    on:search />
                <PosterTable title={"2202"}
                    sessions={[{label:"1PA-", items:range(49,64)}]}
                    on:search />
                <PosterTable title={"2203"}
                    sessions={[{label:"1PA-", items:range(65,80)}]}
                    on:search />
                <PosterTable title={"2204"}
                    sessions={[
                        {label:"1PA-", items:range(81,89)},
                        {label:"1PB-", items:range(1,7)},
                    ]}
                    on:search />
                <PosterTable title={"2207"}
                    sessions={[
                        {label:"1PB-", items:range(8,16)},
                        {label:"1PC-", items:range(1,7)},
                    ]}
                    on:search />
                <PosterTable title={"2208"}
                    sessions={[
                        {label:"1PC-", items:range(8,13)},
                        {label:"1PD-", items:range(1,10)},
                    ]}
                    on:search />
                <PosterTable title={"2209"}
                    sessions={[
                        {label:"1PD-", items:range(11,17)},
                        {label:"1PE-", items:range(1,9)},
                    ]}
                    on:search />
                <PosterTable title={"2210"}
                    sessions={[
                        {label:"1PE-", items:range(10,11)},
                        {label:"1PF-", items:range(1,14)},
                    ]}
                    on:search />
                <PosterTable title={"2211"}
                    sessions={[
                        {label:"1PF-", items:range(15,30)},
                    ]}
                    on:search />
                <PosterTable title={"2212"}
                    sessions={[
                        {label:"1PF-", items:range(31,47)},
                    ]}
                    on:search />
            </div>
        </div>
    </TabPanel>

    <TabPanel>
        <div class="container">
            <div class="panel">
                <SessionTable title={"Oral session"}
                    sessions={project.sessions2}
                    timebins={project.bins_am}
                    slots={project.slots_am}
                    on:search />
                <SessionTable title={"Oral session"}
                    sessions={project.sessions2}
                    timebins={project.bins_pm}
                    slots={project.slots_pm}
                    on:search />
            </div>
            <div class="panel">
                <PosterTable title={"2215"}
                    sessions={[{label:"1PA-", items:range(1,16)}]}
                    on:search />
                <PosterTable title={"2216"}
                    sessions={[{label:"1PA-", items:range(17,32)}]}
                    on:search />
                <PosterTable title={"2201"}
                    sessions={[{label:"1PA-", items:range(33,48)}]}
                    on:search />
                <PosterTable title={"2202"}
                    sessions={[{label:"1PA-", items:range(49,64)}]}
                    on:search />
                <PosterTable title={"2203"}
                    sessions={[{label:"1PA-", items:range(65,80)}]}
                    on:search />
                <PosterTable title={"2204"}
                    sessions={[
                        {label:"1PA-", items:range(81,89)},
                        {label:"1PB-", items:range(1,7)},
                    ]}
                    on:search />
                <PosterTable title={"2207"}
                    sessions={[
                        {label:"1PB-", items:range(8,16)},
                        {label:"1PC-", items:range(1,7)},
                    ]}
                    on:search />
                <PosterTable title={"2208"}
                    sessions={[
                        {label:"1PC-", items:range(8,13)},
                        {label:"1PD-", items:range(1,10)},
                    ]}
                    on:search />
                <PosterTable title={"2209"}
                    sessions={[
                        {label:"1PD-", items:range(11,17)},
                        {label:"1PE-", items:range(1,9)},
                    ]}
                    on:search />
                <PosterTable title={"2210"}
                    sessions={[
                        {label:"1PE-", items:range(10,11)},
                        {label:"1PF-", items:range(1,14)},
                    ]}
                    on:search />
                <PosterTable title={"2211"}
                    sessions={[
                        {label:"1PF-", items:range(15,30)},
                    ]}
                    on:search />
                <PosterTable title={"2212"}
                    sessions={[
                        {label:"1PF-", items:range(31,47)},
                    ]}
                    on:search />
            </div>
        </div>
    </TabPanel>

    <TabPanel>
        <div class="container">
        </div>
    </TabPanel>

    <TabPanel>
        <div class="container">
        </div>
    </TabPanel>
</Tabs>

<style>
    .container {
        width: 100%;
        display: flex;
        flex-flow: row;
        flex-wrap: wrap;
    }
    .panel {
        background-color: #fff;
        border: 1px solid #888;
        border-radius: 15px;

        /* for children */
        display: flex;
        flex-flow: row;
        flex-wrap: wrap;
    }
</style>
