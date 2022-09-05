const app = Vue.createApp({
    data() {
        return {
            org: '',
            topr: 10,
            repo: '',
            stime: '',
            etime: '',
            view: ''
        }
    },
    methods: {
        onSubmitBc(e) {
            console.log(e)
            org = this.org.toLocaleLowerCase()
            topr = this.topr
            const url = 'http://api.django.server:8000/repos'
            let payload = { "org": org, "top": topr }

            document.getElementById('dch').innerHTML = '<center><h1 class="m-5"> Loading Results for your Bar Chart Query ......... <div class="spinner-border text-danger" role="status"><span class="visually-hidden">Loading...</span></div></h1></center> <br><hr><br> <h4 class="mb-5"> You Query Contains Organization: '+org.toLocaleUpperCase()+' for Top '+topr+' Repositories (sorted by Stars) </h4>'

            apiFunc(url, 1, payload)
            this.org = ''
            this.top = ''
        },
        onSubmitLc(e) {
            console.log(e)
            org = this.org
            repo = this.repo
            view = this.view
            stime = new Date(this.stime).toISOString()
            etime = new Date(this.etime).toISOString()
            const url = "http://api.django.server:8000/repos/" + org + "/" + repo + "/commits/"
            let payload = { "since": stime, "until": etime, "view": view }

            document.getElementById('dch').innerHTML = '<center><h1 class="m-5"> Loading Results for your Line Chart Query ......... <div class="spinner-border text-danger" role="status"><span class="visually-hidden">Loading...</span></div></h1></center> <br><hr><br> <h4 class="mb-5"> You Query Contains Organization: '+org.toLocaleUpperCase()+' and Repository: '+repo.toLocaleUpperCase()+' for '+view.toLocaleUpperCase()+view.toLocaleUpperCase()+': view</h4>'

            apiFunc(url, 2, payload)
            this.org = ''
            this.repo = ''
            this.stime = ''
            this.etime = ''
            this.view = ''

        }
    },
    computed: {},
})

async function apiFunc(url, type, payload) {
    console.log("Url - " + url)
    console.log(payload)

    document.getElementById('inputForms').style.display = "none";

    if (type == 1) {
        const response = await fetch(url, {
            method: 'POST',
            body: JSON.stringify(payload),
        })
        if (response.ok) {
            var result = await response.json();
            let source = result.results

            document.getElementById('displayCharts').style.display = 'block';

            document.getElementById('dch').innerHTML = '<center><h2 class="m-3">This is a Bar Chart of ' + org.toLocaleUpperCase() + ' For There Top ' + topr + ' Repositories</h2></center><h3> Following Request took ' + result.total_rps + ' secs </h3> <p> Thereas 1 request to Github APi took ' + result.rps_1 + ' sec (i.e, RPS) Therefore, for total of n requests due to pagination took ' + result.rps_all + ' secs</p>'

            getBarChart(source)

        } else { 
            console.log("Error: \n", response.status);
            document.getElementById('dch').innerHTML = '<center><h2 class="m-3">Organization Name for Bar Chart "' + org.toLocaleUpperCase() + '" is Invalid Or They Might Now have Public Repositories</h2><h3> Please Put a Valid Organization (public on Github)</h3></center>'
            document.getElementById('inputForms').style.display = "block"; }

    } else if (type == 2) {
        const response = await fetch(url, {
            method: 'POST',
            body: JSON.stringify(payload),
        })
        if (response.ok) {
            var result = await response.json();
            let source = result.results

            document.getElementById('displayCharts').style.display = 'block';

            document.getElementById('dch').innerHTML = '<center><h2 class="m-3">This is a Line Chart of ' + org.toLocaleUpperCase() + ' For ' + repo.toLocaleUpperCase() + ' Repository (commits)</h2></center><h3> Following Request took ' + result.total_rps + ' secs </h3> <p> Thereas 1 request to Github APi took ' + result.rps_1 + ' sec (i.e, RPS) Therefore, for total of n requests due to pagination took ' + result.rps_all + ' secs</p>'

            getLineChart(source)

        } else { 
            console.log("Error: \n", response.status); 
            document.getElementById('dch').innerHTML = '<center><h2 class="m-3">Organization Name for Line Chart "' + org.toLocaleUpperCase() + '" For Repo "' + repo.toLocaleUpperCase() + '" is Invalid Or This Repo Does not belong to this Organization</h2><h3> Please Put a Valid Organization and There Corresponding Public Respository</h3></center>'
            document.getElementById('inputForms').style.display = "block"; }
    }

}

function getBarChart(dataset) {
    console.log(dataset)
    var labels = []
    var datasets = []
    var colors = []
    for (let index = 0; index < dataset.length; index++) {
        labels.push(dataset[index].name);
        datasets.push(dataset[index].stars)
        colors.push(getColorCode())
    }
    const barChart = document.getElementById('barChart');
    barChart.style.display = 'block';
    const myChart = new Chart(barChart.getContext('2d'), {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: "Stars",
                data: datasets,
                backgroundColor: colors,
            }]
        },
        options: {
            responsive:true,
          },
    });
}

function getLineChart(dataset) {
    console.log(dataset)
    var labels = []
    var datasets = []
    for (let index = 0; index < dataset.length; index++) {
        labels.push(dataset[index].date);
        datasets.push(dataset[index].commits)
    }
    const lineChart = document.getElementById('lineChart');
    lineChart.style.display = 'block';
    const myChart = new Chart(lineChart.getContext('2d'), {
        type: 'line',
        data: {
            labels: labels,
            datasets: [
                {
                    label: "Commits",
                    fill: false,
                    borderColor: 'rgb(75, 192, 192)',
                    tension: 0.1,
                    data: datasets
                }
            ]
        },
        options: {
            responsive:true,
          },
    });
}

function getColorCode() {
    var makeColorCode = '0123456789ABCDEF';
    var code = '#';
    for (var count = 0; count < 6; count++) {
        code = code + makeColorCode[Math.floor(Math.random() * 16)];
    }
    return code;
}
