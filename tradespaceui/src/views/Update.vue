<template>
  <b-container style="padding: 80px 40px 0 40px">
    <div style="padding-bottom: 30px">
      <div class="mt-3">
        Edit Profile Picture: {{ itemImage ? itemImage.name : "" }}
      </div>
      <br />
      <b-form-file
        v-model="itemImage"
        :state="Boolean(itemImage)"
        placeholder="Choose a file or drop it here..."
        drop-placeholder="Drop file here..."
      ></b-form-file>
    </div>

    <b-form-input
      v-model="location"
      label="Location"
      placeholder="Location"
      style="margin-top: 10px"
      required
    ></b-form-input>

    <b-form-input
      v-model="phone_number"
      label="Phone Number"
      placeholder="Phone Number"
      style="margin-top: 10px"
      required
    ></b-form-input>


    <b-form-input
      v-model="oldEmail"
      label="Old Email"
      placeholder="Old Email"
      style="margin-top: 10px"

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
      <router-link to="/account">
        <v-btn large style="margin-left: 30px" color="secondary"> Cancel </v-btn>
      </router-link>    
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
    newEmailRepeat: "",
    itemImage: null,
    location: ""
  })
};
</script>

<style scoped>
.noHyperlink {
  text-decoration: none;
  color: black;
}

</style>
