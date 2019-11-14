<template>
    <div class="about">
        <h1 style="margin: 80px 0 0 0; padding: 0">Search for: {{$store.getters.search}}</h1>
        <b-row style="padding: 20px 40px 0 40px">
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