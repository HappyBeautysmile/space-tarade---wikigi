<template>
    <v-app>
        <v-app-bar app>
            <v-toolbar-title class="headline text-uppercase">
                <img style="padding: 0; margin: 0" :src="require('@/assets/logo3.png')" height="48" width="50"/>
                <span>Trade</span>
                <span class="font-weight-light">Space</span>
            </v-toolbar-title>
            <v-spacer></v-spacer>
            <v-btn
                    text
                    href="https://github.com/vuetifyjs/vuetify/releases/latest"
                    target="_blank"
            >
                <span class="mr-2">Latest Release</span>
            </v-btn>
        </v-app-bar>
        <v-content>
            <HelloWorld/>
        </v-content>
    </v-app>
</template>

<script>
    import HelloWorld from './components/HelloWorld';

    export default {
        name: 'App',
        components: {
            HelloWorld,
        },
        data: () => ({
            //
        }),
    };
</script>
