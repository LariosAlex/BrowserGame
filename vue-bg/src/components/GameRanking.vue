<template>
  <div>
    <table class='ranking-table table-auto' v-if="!loadingCharacters">
      <thead>
        <tr>
          <th colspan="4"><h2>RANKING</h2></th>
        </tr>
      </thead>
      <thead>
        <tr>
          <th>Posició</th>
          <th>Usuari</th>
          <th>Nickname</th>
          <th>Nivell</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(character, index) in pageCharacters" :key="character.id">
          <td>{{ (parseInt(this.currentPage) * this.charactersPerPage) - (this.charactersPerPage - index - 1)}}</td>
          <td>{{ character.user__username }}</td>
          <td>{{ character.nickname }}</td>
          <td>{{ character.level }}</td>
        </tr>
      </tbody>
    </table>
    <nav class="pagination flex justify-center w-70">
      <ul class="list-style-none flex" v-if="!loadingCharacters">
        <li class="mx-1" @click="getPreviousPage()">
          <a class="relative block rounded-full bg-orange-300 px-3 py-1.5 text-sm text-neutral-600 transition-all duration-300 hover:bg-orange-200 dark:text-white dark:hover:bg-neutral-700 dark:hover:text-white"
            href="">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
              <path stroke-linecap="round" stroke-linejoin="round" d="M11.25 9l-3 3m0 0l3 3m-3-3h7.5M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
          </a>
        </li>
        <li class="mx-1" v-for="page in nPages()" :key="page" :aria-current="page == this.currentPage ? 'page' : false" @click="getRanking(page)">
          <a class="relative block rounded-full bg-orange-300 px-3 py-1.5 text-sm text-neutral-600 transition-all duration-300 hover:bg-orange-200  dark:text-white dark:hover:bg-neutral-700 dark:hover:text-white"
            href="" :class="{ 'bg-orange-400': (this.currentPage == page) }">{{ page }}
            <span v-if="page == this.currentPage" class="absolute -m-px h-px w-px overflow-hidden whitespace-nowrap border-0 p-0 [clip:rect(0,0,0,0)]">(current)</span>
          </a>
        </li>
        <li class="mx-1" @click="getNextPage()">
          <a class="relative block bg-orange-300 rounded-full px-3 py-1.5 text-sm text-neutral-600 transition-all duration-300 hover:bg-orange-200 dark:text-white dark:hover:bg-neutral-700 dark:hover:text-white"
            href="">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
              <path stroke-linecap="round" stroke-linejoin="round" d="M12.75 15l3-3m0 0l-3-3m3 3h-7.5M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
          </a>
        </li>
      </ul>
      </nav>
  </div>
</template>

<script>
export default {
  name: 'RankingList',
  data() {
    const url = new URL(window.location.href);
    if (!url.searchParams.has('p') || !url.searchParams.has('c')){
      url.searchParams.append('p', 1);
      url.searchParams.append('c', 100);
    }
    window.history.replaceState({state: ''}, '', url);
    return {
      currentPage: url.searchParams.get('p'),
      charactersPerPage: url.searchParams.get('c'),
      characters: [],
      pageCharacters: [],
      loadingCharacters: true,
    }
  },
  methods: {
    nPages() {
      return Math.ceil(this.characters.length / this.charactersPerPage)
    },

    async getRanking(pageNumber = this.currentPage) {
      const url = new URL(window.location.href);
      url.searchParams.set('p', pageNumber);
      window.history.replaceState({state: ''}, '', url);
      let minCharacter = (pageNumber * this.charactersPerPage) - this.charactersPerPage
      let maxCharacter = (pageNumber * this.charactersPerPage)
      try {
        const response = await fetch(`/api/getRanking`);
        const data = await response.json();
        this.characters = data.characters;
        this.pageCharacters = this.characters.slice(minCharacter, Math.min(maxCharacter, this.characters.length))
        this.loadingCharacters = false;
      } catch (error) {
        console.error(error);
        this.loadingCharacters = false;
      }
    },

    getPreviousPage(){
      if(this.currentPage > 1){
        this.currentPage--;
        this.getRanking(this.currentPage);
      }
    },

    getNextPage(){
      if(this.currentPage < this.nPages()){
        this.currentPage++;
        this.getRanking(this.currentPage);
      }
    }
  },
  created() {
    this.getRanking()
  },
  watch: {
    charactersPerPage() {
      this.getRanking(this.currentPage)
    }
  }
}
</script>