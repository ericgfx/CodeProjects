console.log = function () { }
const { expect } = require('chai');
const rewire = require('rewire');

describe('', function () {
  it('', function () {
    let appModule;
    try {
        appModule = rewire("../app.js")
    } catch (e) {
        expect(true, 'Try checking your code again. You likely have a syntax error.').to.equal(false);
    }

    let noun1;
    try {
        noun1 = appModule.__get__("noun1");
    } catch (e) {
        expect(true, 'Did you accidentally delete `noun1`?').to.equal(false);
    }
    expect(noun1, 'Did you assign a string value to `noun1`?').to.be.a('string')
    expect((noun1 != '____'), "Did you change `noun1` so that it is not assigned a value of '____'?").to.be.true
    
    let adjective
    try {
        adjective = appModule.__get__("adjective");
    } catch (e) {
        expect(true, 'Did you accidentally delete `adjective`?').to.equal(false);
    }
    expect(adjective, 'Did you assign a string value to `adjective`?').to.be.a('string')
    expect((adjective != '____'), "Did you change `adjective` so that it is not assigned a value of '____'?").to.be.true
    
    let noun2
    try {
        noun2 = appModule.__get__("noun2");
    } catch (e) {
        expect(true, 'Did you accidentally delete `noun2`?').to.equal(false);
    }
    expect(noun2, 'Did you assign a string value to `noun2`?').to.be.a('string')
    expect((noun2 != '____'), "Did you change `noun2` so that it is not assigned a value of '____'?").to.be.true
    
    let verb
    try {
        verb = appModule.__get__("verb");
    } catch (e) {
        expect(true, 'Did you accidentally delete `verb`?').to.equal(false);
    }
    expect(verb, 'Did you assign a string value to `verb`?').to.be.a('string')
    expect((verb != '____'), "Did you change `verb` so that it is not assigned a value of '____'?").to.be.true
    let noun3 
    try {
        noun3 = appModule.__get__("noun3");
    } catch (e) {
        expect(true, 'Did you accidentally delete `noun3`?').to.equal(false);
    }
    expect(noun3, 'Did you assign a string value to `noun3`?').to.be.a('string')
    expect((noun3 != '____'), "Did you change `noun3` so that it is not assigned a value of '____'?").to.be.true
  });
});
