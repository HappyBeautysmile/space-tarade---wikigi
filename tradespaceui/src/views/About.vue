<template>
    <div class="about">
        <b-row style="padding: 80px 40px 0 40px">
            <h1>Search for: {{$store.getters.search}}</h1>
            <li v-for="item in items" v-bind:key="item" style="list-style-type:none;">
                <Item :item="item"></Item>
            </li>
        </b-row>
    </div>
</template>

<script>
    import Item from '../components/item';

    export default {
        name: 'About',
        components: {
            Item,
        },
        data: () => ({
            items: [
                'foo', 'bar', 'bork', 'dog', 'shoe', 'catch', 'p1', 'p2'
            ]
        }),
    };
</script>

<style scoped>

</style>