<script context="module">
    // get from local storage
    let checked = new Set();

	onMount( () => {
        if (window.localStorage.hasOwnProperty("checked")){
            checked = new Set(window.localStorage.checked.split(" "));
        }
	});

    export function add(item){
        checked.add(item);
    }

    export function delete(item){
        checked.delete(item);
    }

    export function has(item){
        return checked.has(item);
    }

    export function store(){
        var s = Array.from(checked).join(" ");
        //fv.innerHTML = s;
        window.localStorage.checked = s;
    }
</script>