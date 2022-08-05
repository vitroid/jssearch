<script>
    import PosterTable from "./postertable.svelte";
	import { Tabs, TabList, TabPanel, Tab } from './Components/Tabs/tabs.js';

    function range(a,b){
        let c = new Set();
        for(let i=a; i<=b; i++){
            c.add(i);
        }
        return c;
    }

    const poster1 = [ { label:"PA1-", items:range(1,74) },
                      { label:"PB1-", items:range(1,15) },
                      { label:"PC1-", items:range(1,16) },
                      { label:"PD1-", items:range(1,14) },
                      { label:"PE1-", items:range(1,10) },
                      { label:"PF1-", items:range(1,42) } ];

</script>

<Tabs>
    <TabList>
        <Tab>Sep. 16</Tab>
        <Tab>Sep. 17</Tab>
        <Tab>Sep. 18</Tab>
        <Tab>Sep. 19</Tab>
        <Tab>協賛企業</Tab>
    </TabList>

    <TabPanel>
        <PosterTable title={"test poster 1"} sessions={poster1} on:search />
    </TabPanel>

    <TabPanel>
    </TabPanel>

    <TabPanel>
    </TabPanel>

    <TabPanel>
    </TabPanel>

    <TabPanel>
    </TabPanel>
</Tabs>


