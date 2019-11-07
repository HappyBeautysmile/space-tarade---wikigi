<template>
    <v-app style="margin: 0; padding: 0">
        <v-app-bar app>
            <v-toolbar-title class="headline text-uppercase">
                <img style="padding: 0; margin: 0" :src="require('@/assets/logo3.png')" height="48" width="50"/>
                <span>Trade</span>
                <span class="font-weight-light">Space</span>
            </v-toolbar-title>
            <v-spacer></v-spacer>
            <router-link to="/about">
                <v-btn text>
                    <span class="mr-2">For trade</span>
                </v-btn>
            </router-link>
        </v-app-bar>
        <v-content style="margin: 0; padding: 0">
<!--            <HelloWorld/>-->
            <router-view></router-view>
        </v-content>
    </v-app>
</template>

<script>
    // import HelloWorld from './components/HelloWorld';

    export default {
        name: 'App',
        // components: {
        //     HelloWorld,
        // },
        data: () => ({
            //
        }),
    };
</script>
