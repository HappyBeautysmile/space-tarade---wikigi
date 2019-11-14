<template>
  <b-container fluid style="padding: 80px 40px 0 40px">
    <div style="padding-bottom: 30px">
      <div class="mt-3">
        Clothing Images: {{ itemImage ? itemImage.name : "" }}
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
      v-model="itemTitle"
      label="Item Title"
      placeholder="Item Title (e.g. Adidas shoes and a green dress)"
      required
    ></b-form-input>

    <b-form-input
      v-model="location"
      label="Location"
      placeholder="Location"
      style="margin-top: 10px"
      required
    ></b-form-input>

    <div style="margin-top: 10px">
      <b-form-input
        v-model="newTag"
        v-on:keyup.enter.native="addTag"
        placeholder="Tags"
        style="margin-bottom:15px"
      ></b-form-input>

      <ul>
        <v-btn
          v-on:click="removeTag(tag.name)"
          style="margin-right:20px"
          v-for="tag in tags"
          v-bind:key="tag.name"
          >{{ tag.name }}</v-btn
        >
      </ul>
    </div>

    <div>
      <b-form-textarea
        id="textarea"
        v-model="description"
        placeholder="Describe your lit af clothings..."
        rows="3"
        max-rows="6"
      ></b-form-textarea>

      <pre class="mt-3 mb-0">{{ description }}</pre>
    </div>

    <div style="padding: 10px">
      <v-btn large color="primary"> Submit</v-btn>
      <v-btn large style="margin-left: 30px" color="secondary"> Cancel </v-btn>
    </div>
  </b-container>
</template>

<script>
export default {
  data: () => ({
    location: "",
    name: "Nikita",
    itemTitle: "",
    tags: [],
    itemImage: null,
    newTag: "",
    imageData: null,
    description: ""
  }),

  methods: {
    successUpload() {
      this.$vs.notify({
        color: "success",
        title: "Upload Success",
        text: "Upload Suceeded"
      });
    },
    addTag() {
      this.tags.push({ name: this.newTag });
      this.newTag = "";
    },
    removeTag(tagToRemove) {
      this.tags = this.tags.filter(item => item.name != tagToRemove);
    }
  }
};
</script>

<style scoped>
.dropbox {
  outline: 2px dashed grey; /* the dash box */
  outline-offset: -10px;
  background: lightcyan;
  color: dimgray;
  padding: 10px 10px;
  min-height: 200px; /* minimum height */
  position: relative;
  cursor: pointer;
}

.input-file {
  opacity: 0; /* invisible but it's there! */
  width: 100%;
  height: 200px;
  position: absolute;
  cursor: pointer;
}

.dropbox:hover {
  background: lightblue; /* when mouse over to the drop zone, change color */
}

.dropbox p {
  font-size: 1.2em;
  text-align: center;
  padding: 50px 0;
}
</style>
