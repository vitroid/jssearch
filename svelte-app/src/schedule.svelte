<script>
    import { _ } from 'svelte-i18n';
    import AsyncTable from "./asynctable.svelte";
    import AwardTable from "./awardtable.svelte";
    import { Tab,TabList,TabPanel,Tabs } from './Components/Tabs/tabs.js';
    import { project } from './jscc72.js';
    import PosterTables from "./PosterTables.svelte";
    import PosterTables2 from "./PosterTables2.svelte";
    import SessionTable from "./sessiontable.svelte";
</script>

<Tabs>
    <TabList>
        <Tab>{$_("sept26")}</Tab>
        <Tab>{$_("sept27")}</Tab>
        <Tab>{$_("sept28")}</Tab>
        <Tab>{$_("Supporters")}</Tab>
    </TabList>

    <TabPanel>
        <div class="container">
            <div class="panel">
                <h1>
                    {$_("Oral sessions")}
                </h1>
                <SessionTable title={$_("Morning sessions")}
                    sessions={project.sessions1}
                    timebins={project.bins_am}
                    slots={project.slots_am}
                    on:search />
                <AsyncTable table={project.symposia} colnames={project.rooms_sy} title={$_("Symposia")} on:search/>
            </div>
            <div class="panel">
                <h1>
                    {$_("Poster sessions")}
                </h1>
                <PosterTables on:search/>
            </div>
        </div>
    </TabPanel>

    <TabPanel>
        <div class="container">
            <div class="panel">
                <h1>
                    {$_("Oral sessions")}
                </h1>
                <SessionTable title={$_("Morning sessions")}
                    sessions={project.sessions2}
                    timebins={project.bins_am}
                    slots={project.slots_am}
                    on:search />
                <AwardTable title={$_("Award lectures")}
                    rooms={project.rooms_aw2}
                    timebins={project.bins_aw2}
                    button_titles={project.titles_aw2}
                    ids={project.ids_aw2}
                    on:search/>
                <SessionTable title={$_("Afternoon sessions")}
                    sessions={project.sessions2}
                    timebins={project.bins_pm}
                    slots={project.slots_pm}
                    on:search />
            </div>

            <div class="panel">
                <h1>
                    {$_("Poster sessions")}
                </h1>
                <PosterTables2 on:search/>
            </div>
        </div>
    </TabPanel>

    <TabPanel>
        <div class="container">
            <div class="panel">
                <h1>
                    {$_("Award lectures")}
                </h1>
                <AwardTable title={$_("Fukuoka International Congress Center")}
                    rooms={project.rooms_aw}
                    timebins={project.bins_aw}
                    button_titles={project.titles_aw}
                    ids={project.ids_aw}
                    on:search/>
            </div>
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
        margin: 5px 0px 5px 0px;
    }
    .panel {
        background-color: #fff;
        border: 1px solid #888;
        border-radius: 15px;

        /* for children */
        display: flex;
        flex-flow: row;
        flex-wrap: wrap;
        justify-content: center;
    }
    h1 {
        background-color: #5ab4bd;
        width: 100%;
        padding: 10px;
        margin: 0px;
        font-size: 120%;
        border-radius: 15px 15px 0px 0px;
        color: white;
    }
</style>
