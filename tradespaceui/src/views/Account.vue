<template>
    <div class="account">
        <b-row style="padding: 80px 40px 0 40px">
            <li v-for="item in items" v-bind:key="item" style="list-style-type:none;">
                <Item :item="item"></Item>
            </li>
        </b-row>
    </div>
</template>

<script>
    import Item from '../components/item';

    export default {
        name: 'Account',
        components: {
            Item,
        },
        data: () => ({
            items: [
                'foo', 'bar'
            ]
        }),
    };
</script>

<style scoped>

</style>