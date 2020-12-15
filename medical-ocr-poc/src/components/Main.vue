<template>
<div style="text-align:left">
  <el-row >
      <el-col :span="6">
        <h1>Step 1: Upload</h1>
        <el-upload style="margin-right: 50px;"
          class="upload-demo"
          drag
          ref="upload"
          accept=".pdf"
          :auto-upload="false"
          :data="data"
          action="http://0.0.0.0:5001/ocr"
          :on-success="onSuccess">
          <i class="el-icon-upload"></i>
          <div class="el-upload__text">Drop file here or <em>click to upload</em></div>
          <div class="el-upload__tip" slot="tip">Only PDF files are allowed.</div>
        </el-upload>
        <el-button style="margin-top: 10px;" size="small" type="success" @click="submitUpload">Upload to server</el-button>
      </el-col>
      <el-col :span="18" class="result">
        <h1>Result</h1>

        <div style="width: 600px;" v-if="records['patient']">
          <div v-for="(item,index) in records['patient']" :key="index">
              <label>{{ index }}</label>
              <el-input :value="item"></el-input>
              <br><br>
            
          </div>
          <div>
            <h2>Text</h2>
            <el-input :value="records['text']" type="textarea" rows="20"></el-input>  
          </div>
        </div>
        <span v-else>Please select PDF first</span>
      </el-col>
    </el-row>
    </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'Main',
  methods: {
    onSuccess(response){
      this.records = response;
      if(this.loading){
        this.loading.close();
      }
    },
    submitUpload() {
      this.loading = this.$loading({
          lock: true,
          text: 'Loading',
          spinner: 'el-icon-loading',
      });
      this.$refs.upload.submit();
    }
  },
  data () {
    return {
      loading: null,
      records: {},
      data: {
        format: 'format1'
      }
    }
  },
  mounted(){
    // axios.get("https://api.myjson.com/bins/1a4mlg")
    //   .then((res) => {
    //     this.records = res['data'];
    //   })
  }
}
</script>

<style >
  .el-upload{
    display: block;
  }
  .el-upload-dragger{
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
  .result *{
    text-transform: uppercase !important;
  }
</style>