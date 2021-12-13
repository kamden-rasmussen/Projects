#include "GlutApp.h"
#include "glut_app.h"
#include "image_menu.h"

GlutApp::GlutApp(int height, int width)
  : mHeight(height), mWidth(width), mActionData(mInputStream, mOutputStream), mMinX(-2.0), mMaxX(2.0), mMinY(-2.0), mMaxY(2.0), 
  mInteractionMode(IM_FRACTAL), mFractalMode(M_MANDELBROT), mMaxNumber(200), mColor1(217, 217, 25), mColor2(120,81,169), mColor3(192, 192, 192), mNumColor(32), 
  mAntiAliasReductionCount(2), mAntiAlias(false) {
  mActionData.setGrid(new ComplexFractal);
  configureMenu(mMenuData);
  setColorTable();
  createFractal();

}

void GlutApp::setSize(int height, int width) {
  mHeight = height;
  mWidth = width;
}

int GlutApp::getHeight() const {
  return mHeight;
}
int GlutApp::getWidth() const {
  return mWidth;
}

void GlutApp::display() {
  //std::cerr << mInteractionMode << std::endl;
  
  glBegin( GL_POINTS );
  
  if( mInteractionMode == IM_FRACTAL){
    PPM& p = mActionData.getOutputImage();
    double max = static_cast<double>(p.getMaxColorValue());
    double r, g, b;
    int row, column;
    for(row = 0; row < p.getHeight(); row++) {
      for(column = 0; column < p.getWidth(); column++) {
        r = p.getChannel(row, column, 0) / max;
        g = p.getChannel(row, column, 1) / max;
        b = p.getChannel(row, column, 2) / max;
        glColor3d(r, g, b);
        glVertex2i(column, p.getHeight()-row-1);
      }
        //std::cerr << "printed everything" << std::endl;
    }
  }

  else if( mInteractionMode == IM_COLORTABLE || mInteractionMode == IM_COLOR1 || mInteractionMode == IM_COLOR2 || mInteractionMode == IM_COLOR3){
    displayColorTable();
  }
  else{
    std::cerr << "failure on mode set" << std::endl;
  }

  glEnd( );
}

void GlutApp::createJulia() {
  selectJulia();
  configureGrid(200);
  juliaParameters(-0.7269, 0.1889);
  fractalPlaneSize(-2.0, 2.0, -2.0, 2.0);
  fractalCalculate();
  gridApplyColorTable();
}

void GlutApp::createJulia2(){
  selectJulia();
  configureGrid(200);
  juliaParameters(-0.4, 0.6);
  fractalPlaneSize(-2.0, 2.0, -2.0, 2.0);
  fractalCalculate();
  gridApplyColorTable();
}

void GlutApp::createMandelbrot(){
  selectMandelbrot();
  configureGrid(200);
  fractalPlaneSize(-2.0, 2.0, -2.0, 2.0);
  fractalCalculate();
  gridApplyColorTable();
}

void GlutApp::createMandelbrot2(){
  selectMandelbrot();
  configureGrid(150);
  fractalPlaneSize(-.40, .10, .60, 1.1);
  fractalCalculate();
  gridApplyColorTable();
}

void GlutApp::createComplexFractal(){
  selectComplexFractal();
  configureGrid(200);
  fractalPlaneSize(-2.0, 2.0, -2.0, 2.0);
  fractalCalculate();
  gridApplyColorTable();
}

void GlutApp::createComplexFractal2(){
  selectComplexFractal();
  configureGrid(1005);
  fractalPlaneSize(-2.0, 2.0, -2.0, 2.0);
  fractalCalculate();
  gridApplyColorTable();
}

void GlutApp::selectJulia(){

  // julia
  mOutputStream.clear();
  mOutputStream.str("");
  mInputStream.clear();
  mInputStream.str("");
  takeAction("julia", mMenuData, mActionData);

  }

void GlutApp::selectMandelbrot(){
      // mandel
  mOutputStream.clear();
  mOutputStream.str("");
  mInputStream.clear();
  mInputStream.str("");
  takeAction("mandelbrot", mMenuData, mActionData);
  
  }

void GlutApp::selectComplexFractal(){
  mOutputStream.clear();
  mOutputStream.str("");
  mInputStream.clear();
  mInputStream.str("");
  takeAction("complex-fractal", mMenuData, mActionData);
  }

void GlutApp::configureGrid(int max){
    // grid
    mOutputStream.clear();
    mInputStream.clear();
    mOutputStream.str("");
    mInputStream.str("");

    if(mAntiAlias){
      std::stringstream tmp;
      tmp << (mHeight * mAntiAliasReductionCount) << " " << (mWidth * mAntiAliasReductionCount) << " " << max;
      mInputStream.str(tmp.str());
    }

    else{
      std::stringstream tmp;
      tmp << mHeight << " " << mWidth << " " << max;
      mInputStream.str(tmp.str());
    }
    takeAction("grid", mMenuData, mActionData);

  }

void GlutApp::juliaParameters(double a, double b){
    mOutputStream.clear();
    mInputStream.clear();
    mOutputStream.str("");
    mInputStream.str("");
    {
      std::stringstream tmp;
      tmp << a << " " << b;
      mInputStream.str(tmp.str());
    }
    takeAction("julia-parameters", mMenuData, mActionData);

  }

void GlutApp::fractalPlaneSize(double x_min, double x_max, double y_min, double y_max){
    // fractal-plane-size
    mOutputStream.clear();
    mInputStream.clear();
    mOutputStream.str("");
    mInputStream.str("");
    {
      std::stringstream tmp;
      tmp << x_min << " " << x_max << " "<< y_min << " " << y_max;
      mInputStream.str(tmp.str());
    }
    takeAction("fractal-plane-size", mMenuData, mActionData);
  }

void GlutApp::fractalCalculate(){
      // fractal-calculate
    mOutputStream.clear();
    mInputStream.clear();
    mOutputStream.str("");
    mInputStream.str("");
    takeAction("fractal-calculate", mMenuData, mActionData);

  }

void GlutApp::gridApplyColorTable(){
    mOutputStream.clear();
    mInputStream.clear();
    mOutputStream.str("");
    mInputStream.str("");
    takeAction("grid-apply-color-table", mMenuData, mActionData);
    applyAntiAlias();
  }

void GlutApp::displayColorTable(){
  for(int column = 0; column <= mWidth; column++){
    //calculate the color value
    double i = column * mActionData.getTable().getNumberOfColors() / mWidth;

    Color color = mActionData.getTable()[i];

    double newRed = color.getRed() / 255.0;
    //std::cerr << "color red " << color.getRed() << std::endl;
    double newBlue = color.getBlue() / 255.0;
    double newGreen = color.getGreen() / 255.0;
    //std::cerr << "red " << newRed << " blue " << newBlue << " green " << newGreen << std::endl;
    glColor3d(newRed, newGreen, newBlue);

    for(int row = 0; row <= mHeight; row++){
      glVertex2i(column, row);
    }
  }
}

void GlutApp::setInteractionMode(InteractionMode mode){
  mInteractionMode = mode;
}

void GlutApp::setColorTable(){
  mOutputStream.clear();
  mInputStream.clear();
  mOutputStream.str("");
  mInputStream.str("");
  {
    std::stringstream tmp;
    tmp << mNumColor;
    mInputStream.str(tmp.str());
  }
  takeAction("set-color-table-size", mMenuData, mActionData);

  mOutputStream.clear();
  mInputStream.clear();
  mOutputStream.str("");
  mInputStream.str("");
  {
    int tempRed1 = mColor1.getRed();
    int tempGreen1 = mColor1.getGreen();
    int tempBlue1 = mColor1.getBlue();
    int tempRed2 = mColor2.getRed();
    int tempGreen2 = mColor2.getGreen();
    int tempBlue2 = mColor2.getBlue();

    std::stringstream tmp;
    tmp << 0 << " " << tempRed1 << " " << tempGreen1 << " " << tempBlue1 << " " << mNumColor / 2 << " " << tempRed2 << " " << tempGreen2 << " " << tempBlue2;
    mInputStream.str(tmp.str());
  }

  takeAction("set-color-gradient", mMenuData, mActionData);

  mOutputStream.clear();
  mInputStream.clear();
  mOutputStream.str("");
  mInputStream.str("");
  {
    int tempRed2 = mColor2.getRed();
    int tempGreen2 = mColor2.getGreen();
    int tempBlue2 = mColor2.getBlue();
    int tempRed3 = mColor3.getRed();
    int tempGreen3 = mColor3.getGreen();
    int tempBlue3 = mColor3.getBlue();

    std::stringstream tmp;
    tmp << mNumColor / 2 << " " << tempRed2 << " " << tempGreen2 << " " << tempBlue2 << " " << mNumColor - 1 << " " << tempRed3 << " " << tempGreen3 << " " << tempBlue3;
    mInputStream.str(tmp.str());
  }
  takeAction("set-color-gradient", mMenuData, mActionData);
}

void GlutApp::decreaseColorTableSize(){
  if(mNumColor > 10){
    mNumColor = (mNumColor / 1.1);
    std::cout << "new Color  " << mNumColor << std::endl;

  // if(mNumColor > 10){
  //   mNumColor = ( (mNumColor / 1.1) );
    setColorTable();
    gridApplyColorTable();
  }
  else{
    std::cerr << " Decrease Less than 10 colors " << std::endl;
  }
}

void GlutApp::increaseColorTableSize(){
  if(mNumColor < 1024){
    mNumColor = (mNumColor * 1.1);
    std::cout << "new Color  " << mNumColor << std::endl;

  // if(mNumColor > 10){
  //   mNumColor = ( (mNumColor / 1.1) );
    setColorTable();
    gridApplyColorTable();
  }
  else{
    std::cerr << " Increase greater than 1024 " << std::endl;
  }
}

void GlutApp::zoomIn(){
  double dx = (1.0 - 0.9)*(mMaxX - mMinX) / 2.0;
  double dy = (1.0 - 0.9)*(mMaxY - mMinY) / 2.0;
  mMinX = mMinX + dx;
  mMaxX = mMaxX - dx;

  mMinY = mMinY + dy;
  mMaxY = mMaxY - dy;
  
}

void GlutApp::zoomOut(){
  double dx = (1.0 - 0.9)*(mMaxX - mMinX) / 2.0;
  double dy = (1.0 - 0.9)*(mMaxY - mMinY) / 2.0;

  double tempMinX = mMinX - dx;
  double tempMaxX = mMaxX + dx;
  double tempMinY = mMinY - dy;
  double tempMaxY = mMaxY + dy;

  if(
    -2.0 <= tempMinX && tempMaxX <= 2.0 &&
    -2.0 <= tempMinY && tempMaxY <= 2.0
  ){
    mMinX = tempMinX;
    mMaxX = tempMaxX;
    mMinY = tempMinY;
    mMaxY = tempMaxY;
  }
}

void GlutApp::moveLeft(){
  double dx = (1.0 - 0.9)*(mMaxX-mMinX) / 2.0;
  if(mMinX - dx >= -2.0){
    mMinX = mMinX - dx;
    mMaxX = mMaxX - dx;
  }
}

void GlutApp::moveRight(){
  double dx = (1.0 - 0.9)*(mMaxX-mMinX) / 2.0;
  if(mMaxX + dx <= 2.0){
    mMinX = mMinX + dx;
    mMaxX = mMaxX + dx;
  }
}

void GlutApp::moveDown(){
  double dy = (1.0 - 0.9)*(mMaxY - mMinY) / 2.0;
  if(mMinY - dy >= -2.0){
    mMinY = mMinY - dy;
    mMaxY = mMaxY - dy;
  }
}

void GlutApp::moveUp(){
double dy = (1.0 - 0.9)*(mMaxY - mMinY) / 2.0;
  if(mMaxY + dy <= 2.0){
    mMinY = mMinY + dy;
    mMaxY = mMaxY + dy;
  }
}

void GlutApp::setFractalMode(FractalMode mode){
  mFractalMode = mode;
}

void GlutApp::increaseMaxNumber(){
  if(mMaxNumber < 2048){
    mMaxNumber = mMaxNumber * 1.1;
    std::cerr << "New Max Number is "<< mMaxNumber << std::endl;
  
  }
  else{
    std::cerr << "New Max Number greater than 2048 " << std::endl;
  }
}

void GlutApp::decreaseMaxNumber(){
  if(mMaxNumber > 11){
    mMaxNumber = mMaxNumber / 1.1;
    std::cerr << "New Max Number is "<< mMaxNumber << std::endl;
  
  }
  else{
    std::cerr << "New Max Number less than 11 " << std::endl;
  }
}

void GlutApp::setAB(int x, int y){

  ComplexFractal *test = dynamic_cast<ComplexFractal *>(&mActionData.getGrid());

  if(mFractalMode == M_MANDELBROT && test != 0){
    mA = mMinX + x * test->getDeltaX();
    mB = mMinY + y * test->getDeltaY();
    std::cerr << "New A " << mA << " New B " << mB << std::endl;
  }

}

void GlutApp::resetPlane(){
  mMinX = -2.0;
  mMaxX = 2.0;
  mMinY = -2.0;
  mMaxY = 2.0;
}

void GlutApp::createFractal(){

  if(mFractalMode == M_MANDELBROT){
    selectMandelbrot();
  }
  else if(mFractalMode == M_JULIA){
    selectJulia();
    juliaParameters(mA, mB);
  }
  else if(mFractalMode == M_COMPLEX){
    selectComplexFractal();
  }

  configureGrid(mMaxNumber);
  fractalPlaneSize(mMinX, mMaxX, mMinY, mMaxY);
  fractalCalculate(); 
  gridApplyColorTable();
  
}

// gui colors
void GlutApp::increaseChannel(Color& color, int channel){
  
  if (color.getChannel(channel) + 10 < 255){
    color.setChannel( channel, (color.getChannel(channel) + 10));
  }
  else{
    color.setChannel(channel, 255);
  }
  setColorTable();
  gridApplyColorTable();
}

void GlutApp::decreaseChannel(Color& color, int channel){

  if(color.getChannel(channel) - 10 > 0){
    color.setChannel(channel, color.getChannel(channel) - 10);
  }
  else{
    color.setChannel(channel, 0);
  }
  setColorTable();
  gridApplyColorTable();
}

Color& GlutApp::fetchColor(){
  if(mInteractionMode == IM_COLOR1){
    return mColor1;
  }
  else if(mInteractionMode == IM_COLOR2){
    return mColor2;
  }
  else if(mInteractionMode == IM_COLOR3){
    return mColor3;
  }
  else{
    static Color mNewColor;
    // // return &mNumColor;
    // // return *mNewColor;
    return mNewColor;
  }

}

void GlutApp::increaseRed(){
  increaseChannel(fetchColor(), 0);
}

void GlutApp::decreaseRed(){
  decreaseChannel(fetchColor(), 0);
}

void GlutApp::increaseGreen(){
  increaseChannel(fetchColor(), 1);
}

void GlutApp::decreaseGreen(){
  decreaseChannel(fetchColor(), 1);
}

void GlutApp::increaseBlue(){
  increaseChannel(fetchColor(), 2);
}

void GlutApp::decreaseBlue(){
  decreaseChannel(fetchColor(), 2);
}

void GlutApp::copyOutputToInput1(){

  mOutputStream.clear();
  mInputStream.clear();
  mOutputStream.str("");
  mInputStream.str("");
  takeAction("copyo1", mMenuData, mActionData);
}

void GlutApp::antiAlias(int reduction_count){

  mOutputStream.clear();
  mInputStream.clear();
  mOutputStream.str("");
  mInputStream.str("");
  {
    std::stringstream tmp;
    tmp << reduction_count;
    mInputStream.str(tmp.str());
  }
  takeAction("anti-alias", mMenuData, mActionData);
}

void GlutApp::applyAntiAlias(){
  if(mAntiAlias){
    copyOutputToInput1();
    antiAlias(mAntiAliasReductionCount);
  }
}

void GlutApp::toggleAntiAlias(){
  if(mAntiAlias){
    mAntiAlias = false;
  }
  else if(mAntiAlias == false){
    mAntiAlias = true;
  }
  else{
    std::cerr << "mAntiAlias error" << std::endl;
  }
}

void GlutApp::increaseAntiAliasReductionCount(){
  mAntiAliasReductionCount += 1;
}

void GlutApp::decreaseAntiAliasReductionCount(){
  int newmAntiAliasReductionCount = mAntiAliasReductionCount - 1;
  if(newmAntiAliasReductionCount < 2){

    mAntiAliasReductionCount =2;
  }
  else{
    mAntiAliasReductionCount = newmAntiAliasReductionCount;
  }
}
