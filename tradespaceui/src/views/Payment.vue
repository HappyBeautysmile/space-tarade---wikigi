<template>
  <b-container style="padding: 80px 40px 0 40px">
    <b-list-group-item
      variant="primary"
      v-for="payment in Payments"
      v-bind:key="payment.num"
      v-on:click="removePayment(payment.num)"
      button
    >
      {{ payment.num }}</b-list-group-item
    >

    <b-form-input
      v-model="newPayment"
      label="New Payment"
      placeholder="New Payment Option"
      style="margin-top: 10px"
      required
    ></b-form-input>

    <div style="padding: 10px">
      <v-btn large color="primary" v-on:click="addPayment(newPayment)">
        Submit</v-btn
      >
      <v-btn large style="margin-left: 30px" color="secondary"> Cancel </v-btn>
    </div>
  </b-container>
</template>

<script>
export default {
  name: "Account",
  components: {},
  data: () => ({
    Payments: [{ num: "1234-1234-1234-1234" }],
    newPayment: ""
  }),
  methods: {
    addPayment() {
      this.Payments.push({ num: this.newPayment.match(/.{1,4}/g).join("-") });
      this.newPayment = "";
    },
    removePayment(paymentNum) {
      this.Payments = this.Payments.filter(item => item.num != paymentNum);
    }
  }
};
</script>

<style scoped>
.noHyperlink {
  text-decoration: none;
  color: black;
}
</style>
