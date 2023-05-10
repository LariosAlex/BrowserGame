<template>
    <table class="action-table table-auto w-full" v-if="!loadingActions">
      <thead>
          <tr>
            <th colspan="5"><h2>ACCIONS</h2></th>
          </tr>
      </thead>
      <thead>
          <tr>
            <th>TIPUS</th>
            <th>ATAC</th>
            <th>EXECUTOR</th>
            <th>OBJECTIU</th>
            <th>EXECUCIÓ</th>
          </tr>
      </thead>
      <tbody>
          <tr v-for="action in actions" :key="action">
              <td>{{ action.action__category }}</td>
              <td>{{ action.action__name }}</td>
              <td>{{ action.performer__nickname }}</td>
              <td v-if=" action.action__category != 'PAS'">{{ action.target__nickname }}</td>
              <td v-else>-</td>
              <td class="text-center flex justify-center items-center">
                <svg v-if="action.succeed" xmlns="http://www.w3.org/2000/svg" fill="green" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                  <path stroke-linecap="round" stroke-linejoin="round" d="M15.182 15.182a4.5 4.5 0 01-6.364 0M21 12a9 9 0 11-18 0 9 9 0 0118 0zM9.75 9.75c0 .414-.168.75-.375.75S9 10.164 9 9.75 9.168 9 9.375 9s.375.336.375.75zm-.375 0h.008v.015h-.008V9.75zm5.625 0c0 .414-.168.75-.375.75s-.375-.336-.375-.75.168-.75.375-.75.375.336.375.75zm-.375 0h.008v.015h-.008V9.75z" />
                </svg>
                <svg v-else xmlns="http://www.w3.org/2000/svg" fill="red" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                  <path stroke-linecap="round" stroke-linejoin="round" d="M15.182 16.318A4.486 4.486 0 0012.016 15a4.486 4.486 0 00-3.198 1.318M21 12a9 9 0 11-18 0 9 9 0 0118 0zM9.75 9.75c0 .414-.168.75-.375.75S9 10.164 9 9.75 9.168 9 9.375 9s.375.336.375.75zm-.375 0h.008v.015h-.008V9.75zm5.625 0c0 .414-.168.75-.375.75s-.375-.336-.375-.75.168-.75.375-.75.375.336.375.75zm-.375 0h.008v.015h-.008V9.75z" />
                </svg> 
              </td>
          </tr>
      </tbody>
    </table>
    <table class="action-table table-auto w-full" v-else>
      <thead>
          <tr>
          <th colspan="3"><h2>CARREGANT ACCIONS</h2></th>
          </tr>
      </thead>
    </table>
</template>
<script>
    export default {
      name: 'CharacterActions',
      data() {
        return {
            actions: null,
            character: null,
          loadingActions: true,
        }
      },
      methods: {
    
        getCharacterActions: async function() {
          try {
            const response = await fetch(`/api/getActionsLog/`+this.character.characterLogged.id);
            const data = await response.json();
            this.actions = data.actions;
            this.loadingActions = false;
          } catch (error) {
            console.error(error);
            this.loadingActions = false;
          }
        },
      },
      mounted() {
        this.character = JSON.parse(document.getElementById('infoCharacter').getAttribute('data'));
        this.getCharacterActions()
        setInterval(this.getCharacterActions, 30000);
      },
    }
    </script>