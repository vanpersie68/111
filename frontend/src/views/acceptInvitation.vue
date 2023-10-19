<template>
  <div class="main">
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <!-- Accept Invitation UI -->
    <div class="window">
      <p class="title">{{ $t('g5.Accept Invitation') }}</p>
      <p class="message">{{ $t('g5.You have been invited to edit the survey')}} </p>
      <p class="surveyname">{{ surveyname }}</p>
      <button class="accept" @click="acceptInvitation">{{ $t('Accept') }}</button>
      <button class="accept" @click="rejectInvitation">{{ $t('Reject') }}</button>
    </div>
  </div>
</template>

<script>
import SurveyServices from '../services/SurveyServices'

export default {
  name: 'AcceptInvitation',
  data() {
    return {
      key: this.$route.query.key,
      surveyid: this.$route.query.id,
      surveyname: '',
    }
  },
  created(){
    this.fetchSurveyName();
  },
  methods: {
    acceptInvitation() {
      if(this.key != 'None'){
        this.$axios
        .post('survey/add-collaborator/', {
          key: this.key,
          surveyid: this.surveyid,
        })
        .then((res) => {
          alert('Congratulations, you have joined the survey group');
        })
        .catch((err) => {
          if (err.response && err.response.data) {
            alert('Error: ' + err.response.data);
            //alert('Backend Error: ' + err.response.data);
          } else {
            alert('Expired link!', err)
          }
          // alert('Expired link!', err)
          window.location.reload()
        })
      }else{
        alert('Please register before accepting the invitation');
        this.$router.push({ name: 'signup', params: { surveyid: this.surveyid } })
      }

    },

    rejectInvitation(){
        alert('You have rejected the invitation');
    },

    async fetchSurveyName(){
       const data = await SurveyServices.getSurvey(this.surveyid)
       this.surveyname = data.name;
    },
  },
}
</script>

<style scoped>
.main {
  position: relative;
  height: 800px;
}

.background {
  width: 100%;
  height: 800px;
  position: relative;
}

.window {
  background-color: white;
  border-radius: 16px;
  padding: 20px 0 18px;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  z-index: 999;
}

.title {
  font-size: 24px;
  font-weight: 700;
  line-height: normal;
  color: black;
  margin-bottom: 20px;
}

.surveyname {
  font-size: 18px;
  font-weight: 500;
  line-height: normal;
  color: orange;
  margin-bottom: 40px;
}

.message {
  width: 400px;
  font-size: 16px;
  font-weight: 400;
  line-height: normal;
  color: dimgray;
  margin-bottom: 20px;
}

.accept {
  background-color: rgba(153, 105, 15, 0.493);
  margin-bottom: 18px;
  border-radius: 8px;
  padding: 13px 100px;
  display: flex;
  align-items: center;
  font-size: 16px;
  font-weight: 400;
  line-height: normal;
}

.accept:hover {
  background-color: blanchedalmond;
  cursor: pointer;
}
</style>