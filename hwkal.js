// Buat Lu Yang Jual Sc Ini Yang Jujur Jangan Samp Nipu Apalagi Lari Dari Tanggung Jawab



const fs = require('fs')
const chalk = require('chalk')

global.gr = 'https://chat.whatsapp.com/xxxx'
global.ig = '@yeftaasyel' // ubah aja
global.email = 'emailanada@gmail.com' //serah
global.region = 'indonesia' // serah
//—————「 Set Nama Own & Bot 」—————//
global.ownername = 'Yefta Asyel' //ubah jadi nama mu, note tanda ' gausah di hapus!
global.domain = 'https://reseller.rizalxalfi.com' // Isi Domain Lu
global.apikey2 = 'ptla_GCTbr872qRTzi8ssOHrXluJs6cvdXXmpS76rOx9pkXW' // Isi Apikey Plta Lu
global.capikey2 = 'ptlc_4fO85Fc8ICGUHAh03lAqt3jW69mW9AHzdt2SS4IlulS' // Isi Apikey Pltc Lu
global.eggsnya = '15' // id eggs yang dipakai
global.location = '1' // id location
//=================================================//
global.owner = ['62827828888'] // ubah aja pake nomor lu
//==========================BY Hw Mods=======================//
global.keyopenai = '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'
//====================BY Hw Mods=============================//
global.botname = 'WeebBot' //ubah jadi nama bot mu, note tanda ' gausah di hapus!
global.packname = 'Yefta Asyel' // ubah aja ini nama sticker
global.author = 'Yefta Asyel' // ubah aja ini nama sticker
global.prefa = ['','!','.',',','🐤','🗿']
global.sessionName = 'yefta'
//Gausah Juga
global.sp = '⭔' // Gausah Juga
global.wlcm = []
global.wlcmm = []
global.anticall = false
//=================================================//
//Gausah Juga
global.limitawal = {
    premium: "Infinity",
    free: 200
}
//=================================================//
let file = require.resolve(__filename)
fs.watchFile(file, () => {
	fs.unwatchFile(file)
	console.log(chalk.redBright(`Update'${__filename}'`))
	delete require.cache[file]
	require(file)
})
