const mongoose = require('mongoose');
const fs = require('fs');
const Tour = require('./../../models/tourModel');

mongoose.connect('mongodb://localhost:27017/natours-test', {
    useNewUrlParser: true,
    useCreateIndex: true,
    useFindAndModify: false
  }).then(con => {
    console.log('DB connection successful!')
  });

  // Read JSON data
  const tours = JSON.parse(fs.readFileSync(`${__dirname}/tours-simple.json`, 'utf-8'));

  // Import Data
  const importData = async () => {
    try {
        await Tour.create(tours)
        console.log('Data successfully loaded')
    } catch (err) {
        console.log(err);
    }
  }

  // Delete data

  const deleteData = async () => {
    try {
        await Tour.deleteMany()
        console.log('Data successfully deleted')
    } catch (err) {
        console.log(err);
    }
  }

  importData()