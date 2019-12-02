<template>
  <b-container fluid style="padding: 5% 0% 0 0%">
    <h1 class="mytradestitle">
      <router-link to="/account">
        <div
          style="position: absolute; padding-left:5%; color:black; font-size:large; margin-top:1%"
        >&lt; BACK</div>
      </router-link>MY TRADES
    </h1>
    <b-card
      no-body
      style="margin-top: 2%; height: 50%; width:100%; margin-right: 2%; display:inline-block;"
      v-for="transaction in trade_list"
      v-bind:key="transaction.trade_id"
    >
      <b-row>
        <v-card-title style="padding-left:5%;">
          <div style="white-space:nowrap">Trade with {{ transaction.other_person.display_name }}</div>
        </v-card-title>
        <b-button
          v-if="transaction.status == 0 || transaction.status == 1"
          class="pushRight"
          variant="danger"
        >Cancel</b-button>
      </b-row>
      <b-row style="display: flex; flex-direction: row; flex-wrap: nowrap; ">
        <b-col
          style="display: flex; flex-direction: column; align-items: center; flex: 1 1 auto; max-width: 26%"
        >
          <img
            :src="transaction.other_person.photo_url"
            style="width: 70%; height: auto; position:relative; border-radius:50%"
          />
          <b-card-body style="text-align: center;">
            <v-list-item-title>
              {{
              transaction.other_person.phone
              }}
            </v-list-item-title>
            <v-list-item-title>
              {{
              transaction.other_person.email
              }}
            </v-list-item-title>
          </b-card-body>
        </b-col>
        <b-col style="flex: 1 1 auto; max-width: 26%">
          <b-card no-body style="height:100%">
            <b-card-title style="padding:5%">Your Item</b-card-title>
            <div
              style="
                  display: flex;
                  flex-direction: column;
                  justify-content: center;
                  align-items: center;
                  "
            >
              <b-img contain color="grey" :src="transaction.your_item_photo" class="imageCard"></b-img>
              <b-card-body>
                <v-list-item-title style="text-align: center">
                  <div style="white-space:normal;">{{ transaction.your_item_name }}</div>
                </v-list-item-title>
              </b-card-body>
            </div>
          </b-card>
        </b-col>
        <b-col style="flex: 1 1 auto; max-width: 26%">
          <b-card no-body style="height:100%">
            <b-card-title style="padding:5%">Their Item</b-card-title>
            <div
              style="
                  display: flex;
                  flex-direction: column;
                  justify-content: center;
                  align-items: center;
                  "
            >
              <b-img contain color="grey" :src="transaction.their_item_photo" class="imageCard"></b-img>
              <b-card-body>
                <v-list-item-title style="text-align: center; ">
                  <div style="white-space:normal;">{{ transaction.their_item_name }}</div>
                </v-list-item-title>
              </b-card-body>
            </div>
          </b-card>
        </b-col>
        <b-col style="flex: 1 1 auto; max-width:22%">
          <b-card-body style="height:100%">
            <div class="pushHalfway">
              <b-card-title>STATUS:</b-card-title>
              <v-list-item-title v-if="transaction.status == 0">Waiting for seller</v-list-item-title>
              <v-list-item-title v-else-if="transaction.status == 1">Waiting for action</v-list-item-title>
              <v-list-item-title v-else-if="transaction.status == 2">In the works</v-list-item-title>
              <v-list-item-title v-else-if="transaction.status == 3">Complete</v-list-item-title>
              <v-list-item-title v-else-if="transaction.status == 4">Cancelled</v-list-item-title>
              <v-list-item-title v-else>Error</v-list-item-title>
            </div>

            <b-button class="pushDown" v-if="transaction.status == 1">Choose Outta Buyer's Shit</b-button>
            <b-button class="pushDown" v-else-if="transaction.status == 2">Complete</b-button>
          </b-card-body>
        </b-col>
      </b-row>
    </b-card>
  </b-container>
</template>

<script>
export default {
  name: "MyTrades",
  components: {},
  data: () => ({
    trade_list: [
      {
        trade_id: "123456",
        other_person: {
          display_name: "nikita",
          phone: "123-456-7890",
          email: "nikita@gmail.com",
          photo_url:
            "https://cdn.shopify.com/s/files/1/0217/3274/products/pau3053_106_h_large.jpg?v=1543863314"
        },
        your_item_photo:
          "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.ebayimg.com%2Fimages%2Fi%2F182533075915-0-1%2Fs-l1000.jpg&f=1&nofb=1",
        your_item_name: "Banana Republic Shirt",
        their_item_photo:
          "https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fi.ebayimg.com%2Fimages%2Fi%2F271404119956-0-1%2Fs-l1000.jpg&f=1&nofb=1",
        their_item_name: "Abercrombie New Fashionable Shirt",
        status: 0
      },
      {
        trade_id: "123456",
        other_person: {
          display_name: "nikita",
          phone: "123-456-7890",
          email: "nikita@gmail.com",
          photo_url:
            "https://cdn.shopify.com/s/files/1/0217/3274/products/pau3053_106_h_large.jpg?v=1543863314"
        },
        your_item_photo:
          "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.Jyd_y8Av2QwWhbkDrFb_6gHaHa%26pid%3DApi&f=1",
        your_item_name: "Banana Republic Shirt",
        their_item_photo:
          "https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fi.ebayimg.com%2Fimages%2Fi%2F271404119956-0-1%2Fs-l1000.jpg&f=1&nofb=1",
        their_item_name: "Abercrombie New Fashionable Shirt",
        status: 1
      },
      {
        trade_id: "123456",
        other_person: {
          display_name: "nikita",
          phone: "123-456-7890",
          email: "nikita@gmail.com",
          photo_url:
            "https://cdn.shopify.com/s/files/1/0217/3274/products/pau3053_106_h_large.jpg?v=1543863314"
        },
        your_item_photo:
          "https://cdn.shopify.com/s/files/1/0217/3274/products/pau3053_106_h_large.jpg?v=1543863314",
        your_item_name: "Banana Republic Shirt",
        their_item_photo:
          "https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fi.ebayimg.com%2Fimages%2Fi%2F271404119956-0-1%2Fs-l1000.jpg&f=1&nofb=1",
        their_item_name:
          "Abercrombie New Fashionable Shirt xxxxxxxxxxxxxxxxx xxxxxxxxxxxxx xxxxxxxxxxxxxx xxxxxx",
        status: 2
      },
      {
        trade_id: "123456",
        other_person: {
          display_name: "nikita",
          phone: "123-456-7890",
          email: "nikita@gmail.com",
          photo_url:
            "https://cdn.shopify.com/s/files/1/0217/3274/products/pau3053_106_h_large.jpg?v=1543863314"
        },
        your_item_photo:
          "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.ebayimg.com%2Fimages%2Fi%2F182533075915-0-1%2Fs-l1000.jpg&f=1&nofb=1",
        your_item_name: "Banana Republic Shirt",
        their_item_photo:
          "https://cdn.shopify.com/s/files/1/0128/9452/products/Puffer-Jacket-FIBL09_959f4782-35d5-40e2-95c9-881682dd440d_1024x1024.png?v=1542326918",
        their_item_name: "Nice Jacket",
        status: 3
      },
      {
        trade_id: "123456",
        other_person: {
          display_name: "nikita",
          phone: "123-456-7890",
          email: "nikita@gmail.com",
          photo_url:
            "https://cdn.shopify.com/s/files/1/0217/3274/products/pau3053_106_h_large.jpg?v=1543863314"
        },
        your_item_photo:
          "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.ebayimg.com%2Fimages%2Fi%2F182533075915-0-1%2Fs-l1000.jpg&f=1&nofb=1",
        your_item_name: "Banana Republic Shirt",
        their_item_photo:
          "https://cdn.shopify.com/s/files/1/0128/9452/products/Puffer-Jacket-FIBL09_959f4782-35d5-40e2-95c9-881682dd440d_1024x1024.png?v=1542326918",
        their_item_name: "Nice Jacket",
        status: 4
      }
    ],
    user_id: "nikita12345"
  })
};
</script>

<style scoped>
.noHyperlink {
  text-decoration: none;
  color: black;
}

.imageSize {
  width: 100%;
  height: 20vw;
  object-fit: cover;
}

.imageCard {
  width: 150px;
  height: 150px;
}

.pushRight {
  margin-left: auto;
  margin-right: 1%;
}

.pushDown {
  position: absolute;
  bottom: 10%;
}

.pushHalfway {
  position: absolute;
  bottom: 50%;
}

.card {
  overflow-wrap: break-word;
  word-wrap: break-word;
  hyphens: auto;
}

.mytradestitle {
  width: 100%;
  margin-top: 2%;
  text-align: center;
}
</style>
