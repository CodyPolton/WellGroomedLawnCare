<template>
  <v-app>
    <v-btn @click="back">Back</v-btn>
    Inovice id = {{id}}
    <v-tabs background-color="grey accent-4" centered class="elevation-2" dark>
      <v-tab key="details">View Invoice</v-tab>
      <v-tab-item >
        <div class="tab-item-wrapper" >
         <ejs-documenteditor id="container"  style="width: 100%;height: 1000px;" :isReadOnly='false' :enablePrint='true' :enableSelection='true' :enableContextMenu='true' :enableSearch='true' :enableOptionsPane='true' :enableWordExport='true' :enableEditor='true' :enableImageResizer='true' :enableEditorHistory='true' :enableHyperlinkDialog='true' :enableTableDialog='true' :enableBookmarkDialog='true' :enableTableOfContentsDialog='true' :enablePageSetupDialog='true' :enableStyleDialog='true' :enableListDialog='true' ></ejs-documenteditor>
          
        </div>
        <span> hello </span>
      </v-tab-item>
      <v-tab key="yards">Jobs</v-tab>
      

    </v-tabs>
  </v-app>
</template>

<script>
import Vue from 'vue';
import { DocumentEditorPlugin, DocumentEditorComponent, Print, SfdtExport, WordExport, TextExport, Selection, Search, Editor, ImageResizer, EditorHistory, ContextMenu, OptionsPane, HyperlinkDialog, TableDialog, BookmarkDialog, TableOfContentsDialog, PageSetupDialog, StyleDialog, ListDialog, ParagraphDialog, BulletsAndNumberingDialog, FontDialog, TablePropertiesDialog, BordersAndShadingDialog, TableOptionsDialog, CellOptionsDialog, StylesDialog } from '@syncfusion/ej2-vue-documenteditor';

Vue.use(DocumentEditorPlugin);
   
// @ is an alias to /src
export default {
  data() {
    return {
      id: null,
      mowprice: null,
      state: null,
      city: null,
      zipcode: null,
      address: null,
      
    };
  },
  name: "Crews",
  components: {},
  created() {
    this.id = this.$route.params.id;
    loadTextFromFile('') 
  },
  methods: {
    back: function() {
      this.$router.go(-1);
    },
    loadTextFromFile: function(ev) {
      const file = ev.target.files[0];
      const reader = new FileReader();
      reader.onload = e => console.log(e.target.result);

      // reader.onload = e => this.$emit("load", e.target.result);
      // reader.readAsText(file);
    }
  }
};
</script>

<style>
 @import "../../node_modules/@syncfusion/ej2-vue-documenteditor/styles/material.css";
</style>