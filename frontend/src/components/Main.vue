<template>
  <div style="text-align: left">
    <h1 class>OCR Document Scanner using Python and Vue</h1>
    <el-row>
      <el-col :span="6">
        <h2 class="el-icon-upload2"> Step 1: Upload</h2>

        <el-upload
          style="margin-right: 50px"
          class="upload-demo"
          drag
          ref="upload"
          accept=".pdf"
          :auto-upload="false"
          :data="data"
          :action="ocr_endpoint"
          :on-success="onSuccess"
        >
          <i class="el-icon-upload"></i>
          <div class="el-upload__text">
            Drop file here or <em>click to upload</em>
          </div>
          <div class="el-upload__tip" slot="tip">
            Only PDF files are allowed.
          </div>
        </el-upload>
        <br />
        <h2 class="el-icon-notebook-2"> Step 2: Select a format</h2>
        <br /><br />
        <el-select v-model="data.format" placeholder="Please select a format">
          <el-option
            v-for="(item, index) in formats"
            v-bind:item="item"
            v-bind:index="index"
            v-bind:key="item.id"
            :value="item.type"
            :label="item.name"
          >
            {{ item.name }}
          </el-option>
        </el-select>
        <br /><br />
        <h2 class="el-icon-magic-stick"> Step 3: Process</h2>
        <br />
        <el-button
          style="margin-top: 10px"
          size="small"
          type="success"
          @click="submitUpload"
          >Process</el-button
        >
      </el-col>
      <el-col :span="18" class="result">
        <div style="width: 600px" v-if="records['data']">
          <div v-for="x in records['data']" :key="x">
            <h2 style="color: navy-blue">{{ x[0] }}</h2>
            <div v-for="y in x[1]" :key="y">
              <label style="color: #006dff">{{ y[0] }}</label>
              <el-input :value="y[1]"></el-input>
              <br /><br />
            </div>
          </div>
          <div>
            <h2>Text</h2>
            <el-input
              :value="records['text']"
              type="textarea"
              rows="20"
            ></el-input>
          </div>
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import axios from "axios";
import API_URL from "../constants";
export default {
  name: "Main",
  methods: {
    onSuccess(response) {
      this.records = response;
      if (this.loading) {
        this.loading.close();
      }
    },
    submitUpload() {
      this.loading = this.$loading({
        lock: true,
        text: "Loading",
        spinner: "el-icon-loading",
      });
      this.$refs.upload.submit();
    },
  },
  data() {
    return {
      ocr_endpoint: API_URL + "/ocr",
      loading: null,
      records: {},
      formats: [{ type: "patient_details", name: "Patient Details" }],
      data: {
        format: "",
      },
    };
  },
};
</script>

<style >
.el-upload {
  display: block;
}
.el-upload-dragger {
  width: 100%;
}
.el-row {
  margin-bottom: 20px;
}
.el-col {
  border-radius: 4px;
}
.bg-purple-dark {
  background: #99a9bf;
}
.bg-purple {
  background: #d3dce6;
}
.bg-purple-light {
  background: #e5e9f2;
}
.grid-content {
  border-radius: 4px;
  min-height: 36px;
}
.row-bg {
  padding: 10px 0;
  background-color: #f9fafc;
}
.result * {
  text-transform: uppercase !important;
}
</style>
