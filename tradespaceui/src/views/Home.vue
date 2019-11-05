<template>
  <div style="margin: 0; padding: 0">
    <b-row style="margin: 60px 0 0 0; padding: 0">
      <!--            <b-col col="1"></b-col>-->
      <b-col col="10" style="text-align: center; padding: 20px 20% 0 20%">
        <img style="padding: 0; margin: 0" :src="require('@/assets/logo3.png')" height="240" width="250"/>
        <div style="font-size: 50px">
          <span>Trade</span>
          <span class="font-weight-light">Space</span>
        </div>
        <div style="padding: 10px">
          <v-btn large> Log in</v-btn>
          <v-btn large style="margin-left: 30px"> Sign up</v-btn>
        </div>
        <div style="font-size: 20px; padding: 0; margin: 0;">
          <p style="font: bold">What is Tradespace ?</p>
          <span class="font-weight-light">TradeSpace is an online platform where you can swap unwanted items like clothing,
                      furniture, etc. with other users. Every time you buy something, there's a chance you won't
                      be able to return it. And if you use it for a while and want to sell it later on, resale value is
                      significantly lower than purchase value. Or you might even have items like furniture that you
                      don't know what to do with when you move. Why deal with this hassle when you can just trade your
                      unwanted items to other people for mutual benefit?
                    </span>
        </div>
      </b-col>
      <!--            <b-col col="1"></b-col>-->
    </b-row>
  </div>
</template>

<script>
  export default {
    data: () => ({}),
  };
</script>
