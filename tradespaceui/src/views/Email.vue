<template>
  <b-container style="padding: 80px 40px 0 40px">
    <b-form-input
      v-model="oldEmail"
      label="Old Email"
      placeholder="Old Email"
      required
    ></b-form-input>

    <b-form-input
      v-model="newEmail"
      label="New Email"
      placeholder="New Email"
      style="margin-top: 10px"
      required
    ></b-form-input>

    <b-form-input
      v-model="newEmail"
      label="New Email2"
      placeholder="Type In Your New Email Again"
      style="margin-top: 10px"
      required
    ></b-form-input>

    <div style="padding: 10px">
      <v-btn large color="primary"> Submit</v-btn>
      <v-btn large style="margin-left: 30px" color="secondary"> Cancel </v-btn>
    </div>
  </b-container>
</template>

<script>
export default {
  name: "Account",
  components: {},
  data: () => ({
    oldEmail: "",
    newEmail: "",
    newEmailRepeat: ""
  })
};
</script>

<style scoped>
.noHyperlink {
  text-decoration: none;
  color: black;
}
</style>
